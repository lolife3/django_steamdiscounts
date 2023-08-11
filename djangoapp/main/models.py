from django.db import models
from django.contrib.auth.models import User


class Discount(models.Model):
    title = models.CharField("Title", max_length=100)
    discount = models.CharField("Discount",max_length=20)
    price = models.CharField("Price", max_length=20)

    def __str__(self):
        return f"{self.title} ({self.discount}) ~ {self.price}"
    
    

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    text = models.TextField("TODOs", null=True, blank=True, max_length=500) 
    complete = models.BooleanField(default=False)
    creation_date = models.DateTimeField("Creation date", auto_now_add=True)
    
    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ["complete"]