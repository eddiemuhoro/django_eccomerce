from django.core.management.base import BaseCommand
from product.models import Product
from orders.models import Order

class Command(BaseCommand):
    help = 'Seed the database with sample orders'

    def handle(self, *args, **kwargs):
        # Fetch existing products
        products = list(Product.objects.all())
        if len(products) < 3:
            self.stdout.write(self.style.ERROR('Not enough products in the database to seed orders.'))
            return

        # Create sample orders using existing products
        orders = [
            {"product": products[0], "quantity": 2, "price": products[0].price * 2},
            {"product": products[1], "quantity": 1, "price": products[1].price},
            {"product": products[2], "quantity": 3, "price": products[2].price * 3},
        ]
        for order in orders:
            Order.objects.create(
                product=order["product"],
                quantity=order["quantity"],
                price=order["price"],
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded sample orders.'))