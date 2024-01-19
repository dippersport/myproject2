

from django.core.management.base import BaseCommand
from myapp.models import Order, Client, Product
from datetime import date

class Command(BaseCommand):
    help = "Create orders."

    def handle(self, *args, **kwargs):
       
        client = Client.objects.first()
        products = Product.objects.all()

        order_data = {
            'client': client,
            'total_amount': sum(product.price for product in products),
            'order_date': date.today(),
        }

        order = Order.objects.create(**order_data)
        order.products.set(products)

        self.stdout.write(self.style.SUCCESS(f'Successfully created order #{order.id}'))
