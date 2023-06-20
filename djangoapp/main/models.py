from django.db import models


class Discounts(models.Model):
    title = models.CharField("Title", max_length=100)
    discount = models.CharField("Discount",max_length=20)
    price = models.CharField("Price", max_length=20)

    def __str__(self):
        return f"{self.title} ({self.discount}) ~ {self.price}"
    