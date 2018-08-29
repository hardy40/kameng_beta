from django.db import models
from django.contrib.auth.models import User


class Time(models.Model):
    time = models.CharField(max_length=20)

    def __str__(self):
        return self.time


class Day(models.Model):
    day = models.CharField(max_length=20)

    def __str__(self):
        return self.day


class MessData(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    s = models.CharField(max_length=30)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Option(models.Model):
    select_option = models.CharField(max_length=50)

    def __str__(self):
        return self.select_option


class MenuObj(models.Model):
    time = models.ForeignKey(Time, on_delete=None)
    day = models.ForeignKey(Day, on_delete=None)
    options = models.ManyToManyField(Option)
