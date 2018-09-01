from django.db import models
from django.contrib.auth.models import User


class KamengitesOrg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    roll = models.IntegerField()
    room = models.CharField(max_length=6)
    # phone = models.IntegerField()

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Secy(models.Model):
    secy = models.OneToOneField(KamengitesOrg, primary_key=True, on_delete=None)
    position = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to="profile", blank=True)
    logos = models.ImageField(upload_to="secy_logos", blank=True)

    def __str__(self):
        return self.position


