from django.shortcuts import render


def facility(request):
    return render(request,'facility/facility.html')
