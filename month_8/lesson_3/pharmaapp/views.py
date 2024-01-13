from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from datetime import time
# Create your views here.

def pharma(request):
    return HttpResponse('My Pharma app')


class CustomerListAPIView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({"Haridorlar ro'yxati":serializer.data})

class CustomerPurchasingListAPIView(APIView):
    def get(self, request, customer_id):
        purchasing = Purchasing.objects.filter(customer_id=customer_id)
        serializer = PurchasingSerializer(purchasing, many=True)
        return Response({"Haridorning haridlari haqida qisqacha ma'lumot":serializer.data})


class PurchasingListAPIView(APIView):
    def get(self, request, med_id):
        purchasing = Purchasing.objects.filter(med_id=med_id)
        serializer = PurchasingSerializer(purchasing, many=True)
        return Response({"Ushbu dorini sotib olgan mijozlar ro'yxati":serializer.data})


class TimeListAPIView(generics.ListAPIView):
    serializer_class = PurchasingSerializer
    def get_queryset(self):
        start_time = time(0, 0)  # 00:00
        end_time = time(23, 0)  # 23:00
        return Purchasing.objects.filter(date__time__range=(start_time, end_time))