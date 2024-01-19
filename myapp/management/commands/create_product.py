# create_product.py

from django.core.management.base import BaseCommand
from myapp.models import Product

class Command(BaseCommand):
    help = "Create products."

    def handle(self, *args, **kwargs):
        products_data = [
            {
                'name': 'Product 1',
                'description': 'Description for Product 1',
                'price': 19.99,
                'quantity': 50,
            },
            {
                'name': 'Product 2',
                'description': 'Description for Product 2',
                'price': 29.99,
                'quantity': 30,
            },
            # Add more products as needed
        ]

        for product_data in products_data:
            product = Product.objects.create(**product_data)
            self.stdout.write(self.style.SUCCESS(f'Successfully created product "{product.name}" with ID {product.id}'))
