# order/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField

class Orders(models.Model):
    email = models.EmailField(unique=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    items = JSONField()
    def __str__(self):
        return f"Order for {self.user.username}"
