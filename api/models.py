from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    data_ago = models.DateField(auto_now=False)

    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=200)
    data_ago = models.DateField(auto_now=False)
  
    def __str__(self) -> str:
        return self.name
    
class Produc(models.Model):
    title = models.CharField(max_length=200)
    amount = models.IntegerField()
    price = models.DecimalField(max_digits=15 , decimal_places=2)

    def __str__(self) -> str:
        return self.title
    
class Order(models.Model):
    customer = models.CharField(max_length=200)
    products = models.ManyToManyField(Produc)
    amount = models.IntegerField()
    name = models.CharField(max_length=200) 
    price = models.DecimalField(max_digits=15 , decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)