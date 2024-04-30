from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(InventoryItem, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
