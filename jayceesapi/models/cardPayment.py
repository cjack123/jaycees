from django.db import models

class CardPayment(models.Model):
    cardHolder = models.CharField(max_length=50)
    cardNumber = models.PositiveSmallIntegerField()
    expDate = models.DateField(max_length=4)
    cardType = models.CharField(max_length=15)
    billingStreet = models.CharField(max_length=50)
    billingCity = models.CharField (max_length=50)
    billingZip = models.PositiveSmallIntegerField()
