from django.contrib import admin
from .models import Employee,Customer,Produc,Order
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','data_ago')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','data_ago')

@admin.register(Produc)
class ProducAdmin(admin.ModelAdmin):
    list_display = ('title','amount','price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','amount','name','price','created','updated',)
    filter_vertical = ('products',)
    print('products',)