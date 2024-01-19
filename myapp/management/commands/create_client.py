
from django.core.management.base import BaseCommand
from myapp.models import Client
from datetime import date

class Command(BaseCommand):
    help = "Create clients."

    def handle(self, *args, **kwargs):
        clients_data = [
            {
                'name': 'Jimmi',
                'email': 'jimmi@example.com',
                'phone_number': '9234345333',
                'address': 'Samara',
                'registration_date': date(2023, 1, 1),
            },
            {
                'name': 'Samir',
                'email': 'another@example.com',
                'phone_number': '1234567890',
                'address': 'Rostov',
                'registration_date': date(2023, 1, 1),
            },
            
        ]

        for client_data in clients_data:
            client = Client.objects.create(**client_data)
            self.stdout.write(self.style.SUCCESS(f'Successfully created client "{client.name}" with ID {client.id}'))
