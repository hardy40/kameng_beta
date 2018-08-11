from django.db import models


class People(models.Model):
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    phone = models.IntegerField()
    designation = models.CharField(max_length=50)
    room = models.CharField(max_length=6)
    image = models.ImageField(upload_to="./logos/", blank=True, null=True)