
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order
from django import forms
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand


class ClientForm(forms.ModelForm):
    
   def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_detail.html', {'client': client})

def client_create(request, pk):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('client_list')

class CreateClientView(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Successfully created client.'))



def order_list(request):
    
    current_user = request.user

    
    end_date = datetime.now()
    start_date_7_days = end_date - timedelta(days=7)
    start_date_30_days = end_date - timedelta(days=30)
    start_date_365_days = end_date - timedelta(days=365)

   
    orders_7_days = Order.objects.filter(customer__user=current_user, order_date__range=[start_date_7_days, end_date]).order_by('order_date')
    orders_30_days = Order.objects.filter(customer__user=current_user, order_date__range=[start_date_30_days, end_date]).order_by('order_date')
    orders_365_days = Order.objects.filter(customer__user=current_user, order_date__range=[start_date_365_days, end_date]).order_by('order_date')

    # Возвращаем результат в шаблон
    return render(request, 'order_list.html', {'orders_7_days': orders_7_days, 'orders_30_days': orders_30_days, 'orders_365_days': orders_365_days})
