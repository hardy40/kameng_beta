from django.db import models


class Kamengite(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField(unique=True)
    room = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return self.room
