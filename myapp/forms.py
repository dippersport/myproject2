from django.db import forms

class Client(forms.Model):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    address = forms.TextField()
    registration_date = forms.DateField(auto_now_add=True)

    def __str__(self):
        return f'Clientname: {self.name}, email: {self.email}, ' f'phone_number: {self.phone_number}, address: {self.address}, ' f'registration_date: {self.registration_date}'        

        

class Product(forms.Model):
    name = forms.CharField(max_length=255)
    description = forms.TextField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.PositiveIntegerField()
    added_date = forms.DateField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}'

class Order(forms.Model):
    client = forms.ForeignKey(Client, on_delete=forms.CASCADE)
    products = forms.ManyToManyField(Product)
    total_amount = forms.DecimalField(max_digits=10, decimal_places=2)
    order_date = forms.DateField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id} by {self.client.name}, Total Amount: {self.total_amount}, Order Date: {self.order_date}'

class Category(forms.Model):
   name = forms.CharField(max_length=50, unique=True)

   def __str__(self):
     return self.name