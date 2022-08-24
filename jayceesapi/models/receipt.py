from django.db import models

class Receipt(models.Model):
    order = models.ForeignKey("order", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits= 7,decimal_places=2)
    paymentMethod = models.ForeignKey("paymentMethod", on_delete=models.CASCADE)
    PaymentAmount = models.DecimalField(max_digits=7,decimal_places=2)
    change = models.DecimalField(max_digits= 7, decimal_places=2)