from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Brand, Employees, Car
from .serializers import BrandSerializer, EmployeeSerializer, CarSerializer


def car(request):
    return HttpResponse('My cars table')

class BrandListAPIView(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response({"Brandlar ro'yxati":serializer.data})

class EmployeeListAPIView(APIView):
    def get(self, request, brand_id):
        employees = Employees.objects.filter(brand_id=brand_id)
        serializer = EmployeeSerializer(employees, many=True)
        return Response({"Branddagi ishchilar haqida qisqacha ma'lumot":serializer.data})

class CarListAPIView(APIView):
    def get(self, request, brand_id):
        cars = Car.objects.filter(brand_id=brand_id)
        serializer = CarSerializer(cars, many=True)
        return Response({"Branddagi mashinalar ro'yxati":serializer.data})

class CarCountAPIView(APIView):
    def get(self, request, brand_id):
        brand = Brand.objects.get(id=brand_id)
        car_count = brand.car_set.count()
        return Response({'Branddagi mashinalar soni': car_count})