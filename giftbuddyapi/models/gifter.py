from django.db import models
from django.contrib.auth.models import User

class Gifter(models.Model):
    """Gifter model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_image_url = models.ImageField()