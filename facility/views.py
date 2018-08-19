from django.shortcuts import render
from accounts.models import Secy


def facility(request):
    secy_list = Secy.objects.all()
    context = {'secy_list': secy_list}
    return render(request,'facility/facility.html', context)
