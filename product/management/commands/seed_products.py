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
            {
                "name": "Product 4",
                "desc": "Description for product 4",
                "price": 150.00,
                "quantity": 12,
            },
            {
                "name": "Product 5",
                "desc": "Description for product 5",
                "price": 250.00,
                "quantity": 7,
            },
            {
                "name": "Product 6",
                "desc": "Description for product 6",
                "price": 175.00,
                "quantity": 15,
            },
            {
                "name": "Product 7",
                "desc": "Description for product 7",
                "price": 220.00,
                "quantity": 3,
            },
            {
                "name": "Product 8",
                "desc": "Description for product 8",
                "price": 90.00,
                "quantity": 20,
            },
            {
                "name": "Product 9",
                "desc": "Description for product 9",
                "price": 120.00,
                "quantity": 6,
            },
            {
                "name": "Product 10",
                "desc": "Description for product 10",
                "price": 180.00,
                "quantity": 4,
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