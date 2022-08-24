from django.db import models

class PaymentMethod(models.Model):
    type = models.ForeignKey("size", on_delete=models.CASCADE)