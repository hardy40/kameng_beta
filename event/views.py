from django.shortcuts import render, HttpResponseRedirect
from accounts.models import Secy
from .models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def posts(request):
    if request.user.is_authenticated:
        post_list = Event.objects.all()[::-1]
        num_posts = len(post_list)
        secy_list = Secy.objects.all()
        page = request.GET.get('page', 1)
        print(page)
        paginator = Paginator(post_list, 3)
        numbers1 = paginator.page(page)
        numbers = []

        for i in range(1, int(page)+1):
            numbers += paginator.page(str(i))
        num_numbers = len(numbers)
        context = {'numbers': numbers, 'numbers1': numbers1, 'secy_list': secy_list, 'val': num_posts-num_numbers}
        return render(request, 'event/event.html', context)
    return HttpResponseRedirect('/login')


def add(request):
    if request.user.is_authenticated:
        secys = Secy.objects.all()
        context = {'secy_list': secys}
        p = Event()
        for s in secys:
            if s.secy.user == request.user:
                if request.method == 'POST':
                    image = request.FILES.get('file')
                    p.img = image
                    p.user = request.user
                    p.post = request.POST.get('txt')
                    p.save()
                return render(request, 'event/post_event.html', context)
        return render(request, 'event/not_secy.html')
    return HttpResponseRedirect('/login')

