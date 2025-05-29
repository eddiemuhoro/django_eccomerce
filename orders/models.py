from django.db import models
from product.models import Product

# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.product} x {self.quantity}"
    
    class Meta:
        ordering = ['-order_date']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'