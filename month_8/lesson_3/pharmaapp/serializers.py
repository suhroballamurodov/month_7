from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class PharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacist
        fields = '__all__'

class MedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicines
        fields = '__all__'

class SalesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sales
        fields = '__all__'

class PurchasingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only = True)
    class Meta:
        model = Purchasing
        fields = '__all__'

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'