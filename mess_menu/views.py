from django.shortcuts import render, HttpResponseRedirect
from accounts.models import KamengitesOrg, Secy
from .models import MessData, MenuObj, Option, Time, Day


def mess_response(request):
    if request.user.is_authenticated:
        menu_obj_list = MenuObj.objects.all()
        time_list = Time.objects.all()
        day_list = Day.objects.all()
        i = 0
        context = {'menu_obj_list': menu_obj_list, 'time_list': time_list, 'day_list': day_list,'i':i}
        return render(request, 'mess_menu/mess.html', context)
    else:
        return HttpResponseRedirect('/login')


def submitted(request):
    if request.method == "POST":
        r = MessData()
        menu_obj_list = MenuObj.objects.all()
        k = KamengitesOrg.objects.filter(user=request.user)
        r.user = k[0].user
        r.s = ""
        for obj in menu_obj_list:
            r.s += str(request.POST.get(str(obj)))
            for o in obj.options.all():
                if str(o.value) == str(request.POST.get(str(obj))):
                    print(1)
                    o.count = o.count + 1
                    o.save()
        r.save()
        return render(request, 'mess_menu/Submitted.html')