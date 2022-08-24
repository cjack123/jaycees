from django.db import models

class Flavor(models.Model):
    flavor = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7,decimal_places=2)