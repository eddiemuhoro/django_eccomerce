from django.core.management.base import BaseCommand
from product.models import Product

class Command(BaseCommand):
    help = 'Seed the database with initial products'

    def handle(self, *args, **kwargs):
        products = [
            {
                "name": "Product 1",
                "desc": "Description for product 1",
                "price": 100.00,
                "quantity": 10,
            },
            {
                "name": "Product 2",
                "desc": "Description for product 2",
                "price": 200.00,
                "quantity": 5,
            },
            {
                "name": "Product 3",
                "desc": "Description for product 3",
                "price": 300.00,
                "quantity": 8,
            },
        ]

        for prod in products:
            Product.objects.get_or_create(
                name=prod["name"],
                defaults={
                    "desc": prod["desc"],
                    "price": prod["price"],
                    "quantity": prod["quantity"],
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded products.'))