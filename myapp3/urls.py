from django.urls import path
from . import views

app_name = 'myapp3'


urlpatterns = [
    path('client_create/<int:client_id>', views.client_create , name='client_create'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_list/<int:client_id>/', views.order_list, name='order_list'),
    
]