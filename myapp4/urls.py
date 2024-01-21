from django.urls import path
from .views import create_product


app_name = 'myapp4'

urlpatterns = [
    
    path('create_product/', create_product, name='create_product'),
   


]


#git remote add origin https://github.com/username/myproject.git
