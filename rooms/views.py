
from django.shortcuts import render, HttpResponseRedirect
# from .models import Kamengite
from accounts.models import KamengitesOrg


def rooms(request):
    kamengites = KamengitesOrg.objects.all()
    m = KamengitesOrg.objects.filter(user=request.user)
    context = {'kamengites': kamengites, 'cur_user': m[0]}
    return render(request, 'rooms/rooms.html', context)


def search(request):
    kamengites = KamengitesOrg.objects.all()
    if request.method == 'POST':
        result = []
        name = request.POST.get('Name')
        rollnum = request.POST.get('Roll')
        roomnum = request.POST.get('Room')
        # print(rollnum)
        if roomnum:
            for kamengite in kamengites:
                if roomnum.lower() in kamengite.room.lower():
                    result.append(kamengite)
            context = {'result': result}
            return render(request, 'rooms/search.html', context)
        if name:
            for kamengite in kamengites:
                if name.lower() in kamengite.user.first_name.lower() \
                        or \
                   name.lower() in kamengite.user.last_name.lower():
                    result.append(kamengite)
            context = {'result': result}
            return render(request, 'rooms/search.html', context)
        # if rollnum == "":
        #     return render(request, 'rooms/empty_fields.html')
        # try:
        #     rollnum = int(rollnum)
        # except ValueError:
        #     return render(request, 'rooms/roll_not_int.html')
        # if rollnum:
        for kamengite in kamengites:
            if rollnum in str(kamengite.roll):
                result.append(kamengite)
        context = {'result': result}
        return render(request, 'rooms/search.html', context)
    return render(request, 'rooms/not_found.html')


# def add_kamengite(request):
#     if request.method == 'POST':
#         k = KamengitesOrg()
#         k.user.name = request.POST.get('Name')
#         k.roll_no = request.POST.get('Roll')
#         k.room = request.POST.get('Room')
#         k.save()
#         kamengites = Kamengite.objects.all()
#         context = {'kamengites': kamengites}
#         # return render(request, 'rooms/rooms.html', context)
#         return HttpResponseRedirect('/rooms', context)
