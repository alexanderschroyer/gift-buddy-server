from django.db import models 

class RecipientInterest(models.Model):
    """Recipient Interest model"""
    interest = models.ForeignKey("Interest", on_delete=models.CASCADE)
    recipient = models.ForeignKey("Recipient", on_delete=models.CASCADE)