# properties/models.py
from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=200)  # required
    description = models.TextField()          # required
    price = models.DecimalField(max_digits=10, decimal_places=2)  # required
    location = models.CharField(max_length=100)  # required
    created_at = models.DateTimeField(auto_now_add=True)  # required

    def __str__(self):
        return f"{self.title} - {self.location}"
