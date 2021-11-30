from django.db import models

class Wishlist(models.Model):
    """Wishlist model"""
    gifter = models.ForeignKey("Gifter", on_delete=models.CASCADE)
    wanted_item = models.CharField(max_length=75)