from django.shortcuts import render, HttpResponseRedirect
from accounts.models import Secy
from .models import Event


def posts(request):
    post_list = Event.objects.all()
    context = {'post_list': post_list}
    return render(request, 'event/event.html', context)


def add(request):
    if request.user.is_authenticated:
        secys = Secy.objects.all()
        p = Event()
        for s in secys:
            if s.secy.user == request.user:
                if request.method == 'POST':
                    image = request.FILES.get('file')
                    p.img = image
                    p.post = request.POST.get('txt')
                    p.save()
                return render(request, 'event/post_event.html')
        return render(request, 'event/not_secy.html')
    return HttpResponseRedirect('/login')

