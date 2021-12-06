from django.db import models


class Recipient(models.Model):
    """Recipient model"""
    gifter = models.ForeignKey("Gifter", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    interests = models.ManyToManyField("Interest", through="RecipientInterest")