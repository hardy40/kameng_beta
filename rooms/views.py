from django.shortcuts import render, HttpResponseRedirect
from accounts.models import KamengitesOrg, Secy


def rooms(request):
    secy_list = Secy.objects.all()
    context = {'secy_list':secy_list}
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
