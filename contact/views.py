from django.shortcuts import render
from .models import People


def contact_us(request):
    s_list = People.objects.all()
    context = {'secy_list': s_list}
    return render(request, 'contact/contact.html', context)
