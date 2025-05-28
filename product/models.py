from django.db import models


def product_image_path(instance, filename):
    return f"products/{instance.id}/{filename}"
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(("Description"), blank=True)
    image = models.ImageField(upload_to=product_image_path, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at']
