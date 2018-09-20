from django.shortcuts import render, HttpResponseRedirect, Http404
from .models import Complaint
from accounts.models import KamengitesOrg, Secy


def complaint(request):
    if request.user.is_authenticated:
        k = KamengitesOrg.objects.filter(user=request.user)
        complaints = Complaint.objects.filter(u=k[0])[::-1]
        secy_list = Secy.objects.all()
        context = {'complaints': complaints, 'secy_list': secy_list}
        return render(request, 'complaints/complaint_user.html', context)
    else:
        return HttpResponseRedirect('/login')


def submit_complaint(request):
    # if request.user.is_authenticated:
        if request.method == 'POST':
            c = Complaint()
            k = KamengitesOrg.objects.filter(user=request.user)
            c.u = k[0]
            c.complaintText = request.POST.get('txt')
            c.type_of_complaint = request.POST.get('toc')
            temp = request.POST.getlist('stud')
            if len(temp):
                c.is_resolved_stud = True
            else:
                c.is_resolved_stud = False
            c.save()
            return HttpResponseRedirect('/complaints')


def secy_complaint(request):
    secy_list = Secy.objects.all()
    for s in secy_list:
        if s.secy.user == request.user:
            c_list = Complaint.objects.filter(type_of_complaint=s.position)[::-1]
            context = {'c_list': c_list, 'secy_list': secy_list}
            return render(request, 'complaints/check.html', context)


def delete(request):
    if request.method == 'POST':
        ct = request.POST.get('d')
        c = Complaint.objects.filter(pk=ct)
        c.delete()
        return HttpResponseRedirect('/complaints')
