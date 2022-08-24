from django.db import models

class Toppings(models.Model):
    toppings = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7,decimal_places=2)
