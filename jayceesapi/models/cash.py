from django.db import models

class Cash(models.Model):
    cash = models.DecimalField(max_digits=7, decimal_places=2)