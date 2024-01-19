from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Clientname: {self.name}, email: {self.email}, ' f'phone_number: {self.phone_number}, address: {self.address}, ' f'registration_date: {self.registration_date}'        

        

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id} by {self.client.name}, Total Amount: {self.total_amount}, Order Date: {self.order_date}'

class Category(models.Model):
   name = models.CharField(max_length=50, unique=True)

   def __str__(self):
     return self.name


