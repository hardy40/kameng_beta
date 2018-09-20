from django.shortcuts import render, HttpResponseRedirect
from accounts.models import Secy
from .models import Event


def posts(request):
    if request.user.is_authenticated:
        post_list = Event.objects.all()[::-1]
        secy_list = Secy.objects.all()
        context = {'post_list': post_list, 'secy_list': secy_list}
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

