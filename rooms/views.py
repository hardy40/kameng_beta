from django.shortcuts import render
from .models import Kamengite


def rooms(request):
    kamengites = Kamengite.objects.all()
    context = {'kamengites': kamengites}
    return render(request, 'rooms/rooms.html', context)


def roll(request):
    kamengites = Kamengite.objects.all()
    if request.method == 'POST':
        result = []
        name = request.POST.get('Name')
        rollnum = request.POST.get('Roll')
        roomnum = request.POST.get('Room')
        # print(rollnum)
        if roomnum:
            for kamengite in kamengites:
                if roomnum == kamengite.room:
                    result.append(kamengite)
            context = {'result': result}
            return render(request, 'rooms/search.html', context)
        if name:
            for kamengite in kamengites:
                if name.lower() in kamengite.name.lower().split(" "):
                    result.append(kamengite)
            context = {'result': result}
            return render(request, 'rooms/search.html', context)
        if rollnum == "":
            return render(request, 'rooms/empty_fields.html')
        try:
            rollnum = int(rollnum)
        except ValueError:
            return render(request, 'rooms/roll_not_int.html')
        if rollnum:
            for kamengite in kamengites:
                if rollnum == kamengite.roll_no:
                    result.append(kamengite)
            context = {'result': result}
            return render(request, 'rooms/search.html', context)
    return render(request, 'rooms/not_found.html')


def add_kamengite(request):
    if request.method == 'POST':
        k = Kamengite()
        k.name = request.POST.get('Name')
        k.roll_no = request.POST.get('Roll')
        k.room = request.POST.get('Room')
        k.save()
        kamengites = Kamengite.objects.all()
        context = {'kamengites': kamengites}
        return render(request, 'rooms/rooms.html', context)
