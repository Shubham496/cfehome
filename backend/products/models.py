from django.db import models
from decimal import Decimal
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return round(float(self.price) * 0.8, 2)

    
    def get_discount(self):
        
        return round(float(self.price)*0.2,2)

