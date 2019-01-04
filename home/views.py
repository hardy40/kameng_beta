from django.shortcuts import render
from accounts.models import Secy


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return ip


def home(request):
    secy_list = Secy.objects.all()
    context = {'secy_list': secy_list}
    print(get_client_ip(request))
    return render(request, 'home/home.html', context)



