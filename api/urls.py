from django.urls import path
from .views import EmployeeDetaill,ClientDetaill
from datetime import datetime

urlpatterns =[
    path('employee/<int:id>/<int:month>/<int:year>/',EmployeeDetaill.as_view(), name = "post-detail"),
    path('Client/<int:id>/<int:month>/<int:year>/',ClientDetaill.as_view(), name = "post-detail")
]



