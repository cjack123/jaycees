from django.db import models

class Order(models.Model):
    orderNumber = models.PositiveSmallIntegerField()
    size = models.ForeignKey("size", on_delete=models.CASCADE)
    flavor = models.ForeignKey("flavor", on_delete=models.CASCADE)
    toppings = models.ForeignKey("toppings", on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=7,decimal_places=2)