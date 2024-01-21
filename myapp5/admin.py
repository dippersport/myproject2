
from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
   queryset.update(quantity=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address', 'registration_date']
    search_fields = ['name', 'email']
    


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'date_added', 'rating'] 
    list_filter = ['date_added', 'price']  
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта(description)'
    fields = ['name', 'quantity', 'date_added', 'rating', 'description', 'price'] 
    readonly_fields = ['date_added', 'rating']

    actions = [reset_quantity]




class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'total_amount', 'order_date']
    filter_horizontal = ('products',)  
    search_fields = ['client__name', 'id']
    


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)