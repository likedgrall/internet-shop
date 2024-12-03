from django.db import models

# Create your models here.

class Snickers(models.Model):
    img = models.ImageField(upload_to='snickers/')
    name = models.CharField(max_length=15)
    description = models.TextField()
    raits = models.FloatField()
    quantity = models.PositiveIntegerField()
    cost = models.PositiveIntegerField()

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    adress = models.TextField(default="1")
    product = models.ForeignKey(Snickers, on_delete=models.SET_NULL, null=True)
