from django.db import models
from django.db.models.fields import related


class Recipient(models.Model):
    """Recipient model"""
    gifter = models.ForeignKey("Gifter", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    interests = models.ManyToManyField("Interest", through="RecipientInterest", related_name="Interests")