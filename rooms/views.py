from django.shortcuts import render, HttpResponseRedirect
from accounts.models import KamengitesOrg


def rooms(request):
    kamengites = KamengitesOrg.objects.all()
    context = {'kamengites': kamengites}
    if request.method == 'POST':
        if request.POST.get('Name') or request.POST.get('Roll') or request.POST.get('Room'):
            # print("check 1")
            result = []
            name = request.POST.get('Name')
            rollnum = request.POST.get('Roll')
            roomnum = request.POST.get('Room')
            if roomnum:
                for kamengite in kamengites:
                    if roomnum.lower() in kamengite.room.lower():
                        result.append(kamengite)
                context = {'kamengites': result}
                return render(request, 'rooms/rooms.html', context)
            if name:
                # print("check 2")
                for kamengite in kamengites:
                    if name.lower() in kamengite.user.first_name.lower() \
                            or \
                            name.lower() in kamengite.user.last_name.lower():
                        # print("check 3")
                        # print(kamengite.user.first_name)
                        result.append(kamengite)
                context = {'kamengites': result}
                # print("check 4")
                return render(request, 'rooms/rooms.html', context)
            for kamengite in kamengites:
                if rollnum in str(kamengite.roll):
                    result.append(kamengite)
            context = {'kamengites': result}
    return render(request, 'rooms/rooms.html', context)


# def search(request):
#     kamengites = KamengitesOrg.objects.all()
    # if request.method == 'POST':
    #     result = []
    #     name = request.POST.get('Name')
    #     rollnum = request.POST.get('Roll')
    #     roomnum = request.POST.get('Room')
    #     if roomnum:
    #         for kamengite in kamengites:
    #             if roomnum.lower() in kamengite.room.lower():
    #                 result.append(kamengite)
    #         context = {'result': result}
    #         return render(request, 'rooms/search.html', context)
    #     if name:
    #         for kamengite in kamengites:
    #             if name.lower() in kamengite.user.first_name.lower() \
    #                     or \
    #                name.lower() in kamengite.user.last_name.lower():
    #                 result.append(kamengite)
    #         context = {'result': result}
    #         return render(request, 'rooms/search.html', context)
    #     for kamengite in kamengites:
    #         if rollnum in str(kamengite.roll):
    #             result.append(kamengite)
    #     context = {'result': result}
    #     return render(request, 'rooms/search.html', context)
    # return render(request, 'rooms/not_found.html')
