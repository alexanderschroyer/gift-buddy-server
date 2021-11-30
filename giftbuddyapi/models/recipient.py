from django.db import models


class Recipient(models.Model):
    """Recipient model"""
    gifter = models.ForeignKey("Gifter", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    interest = models.CharField(max_length=50)