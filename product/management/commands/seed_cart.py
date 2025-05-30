from django.core.management.base import BaseCommand
from product.models import Product, Cart

class Command(BaseCommand):
    help = 'Seed the database with sample orders'

    def handle(self, *args, **kwargs):
        # Fetch existing products
        products = list(Product.objects.all())
        if len(products) < 3:
            self.stdout.write(self.style.ERROR('Not enough products in the database to seed orders.'))
            return

        # Create sample cart using existing products
        cart_items = [
            {"product": products[0], "quantity": 2 },
            {"product": products[1], "quantity": 1 },
            {"product": products[2], "quantity": 3 },
        ]
        for cart in cart_items:
            Cart.objects.create(
                product=cart["product"],
                quantity=cart["quantity"]
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded sample cart items.'))