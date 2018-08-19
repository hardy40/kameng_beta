from django.db import models
from django.contrib.auth.models import User


class KamengitesOrg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True, primary_key=True)
    roll = models.IntegerField()
    room = models.CharField(max_length=6)
    # phone = models.IntegerField()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Secy(models.Model):
    secy = models.OneToOneField(KamengitesOrg, primary_key=True, on_delete=None)
    position = models.CharField(max_length=30)

    def __str__(self):
        return self.position

