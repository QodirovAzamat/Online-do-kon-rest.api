from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee,Order,Customer
from datetime import datetime

# Create your views here.
class EmployeeDetaill(APIView):
    def get(self,request,id,year,month):
        user = Employee.objects.filter(id=id)
        data = list(user.values())
        user_name = data[0]['name']
        order_user = Order.objects.filter(name=user_name)
        order_em = list(order_user.values())
        amount_a = 0
        order_sum = 0
        for i in order_em:
            sana = i['created']
            if sana.year == year and sana.month == month:
                order_sum += (i['price'])
                amount_a += (i['amount'])
        return Response(data=
                        {"Employee": data,
                         "customer_son": amount_a,
                         "order_sum ": order_sum}
                         )
class ClientDetaill(APIView):
    def get(self,request,id,year,month):
        user = Customer.objects.filter(id=id)
        data = list(user.values())
        user_name = data[0]['name']
        customer_user = Order.objects.filter(customer=user_name)
        customer_em = list(customer_user.values())
        amount_a = 0
        order_sum = 0
        for i in customer_em:
            sana = i['created']
            if sana.year == year and sana.month == month:
                order_sum += (i['price'])
                amount_a += (i['amount'])
        return Response(data=
                        {"Customer": data,
                         "customer_son": amount_a,
                         "order_sum ": order_sum}
                         )
        




        