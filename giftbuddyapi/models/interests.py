from django.db import models

class Interest(models.Model):
    """Interest model"""
    label = models.CharField(max_length=150)