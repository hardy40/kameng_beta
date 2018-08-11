from django.db import models


class Kamengite(models.Model):
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    room = models.CharField(max_length=6)
    # function
    def __str__(self):
        return self.name
