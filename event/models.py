from django.db import models


class Event(models.Model):
    post = models.CharField(max_length=500, null=True)
    img = models.ImageField(upload_to="post_images", blank=True)