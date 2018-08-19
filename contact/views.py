from django.shortcuts import render
from accounts.models import Secy


def contact_us(request):
    secy_list = Secy.objects.all()
    context = {'secy_list': secy_list}
    return render(request, 'contact/contact.html', context)
