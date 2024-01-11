from rest_framework import serializers
from .models import Brand, Car, Employees


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'cars', 'employees',]