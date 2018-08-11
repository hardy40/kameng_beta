from django.shortcuts import render
from .models import Kamengite


def rooms(request):
    kamengites = Kamengite.objects.all()
    context = {'kamengites': kamengites}
    return render(request, 'rooms/rooms.html', context)


def roll(request, rollnum):
    kamengites = Kamengite.objects.all()
    for kamengite in kamengites:
        if rollnum == kamengite.roll_no :
            context = {'kamengite', kamengite}
            return render(request, 'rooms/roll_search.html', context)
    return render(request, 'rooms/not_found.html')