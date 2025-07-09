from django.shortcuts import render

from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

# List and Create Employee
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Retrieve, Update, and Delete Employee
class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
