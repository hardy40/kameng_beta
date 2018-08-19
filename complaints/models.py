from django.db import models
from accounts.models import KamengitesOrg


class Complaint(models.Model):
    complaintText = models.CharField(max_length=500)
    is_resolved_ct = models.BooleanField(default=False)
    is_resolved_stud = models.BooleanField(default=False)
    reply = models.CharField(max_length=500)
    type_of_complaint = models.CharField(max_length=20)
    u = models.ForeignKey(KamengitesOrg, on_delete=models.CASCADE)

