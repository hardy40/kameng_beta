from django.db import models
from django.contrib.auth.models import User
from accounts.models import KamengitesOrg


class Event(models.Model):
    post = models.CharField(max_length=500, null=True)
    img = models.ImageField(upload_to="post_images", blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
