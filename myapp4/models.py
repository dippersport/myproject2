from django.db import models
from django.utils import timezone



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    photo = models.ImageField(upload_to='product_photos/', blank=True)  
    customer = models.CharField(max_length=255, default=timezone.now)

    def __str__(self):
        return self.name
    

