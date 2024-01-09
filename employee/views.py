from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from .models import *
from .seriliazer import *

# Create your views here.
class EmployeeView(generics.GenericAPIView):
    model=Employee
    serializer=EmployeeSerializer

    def post(self,request):
        try:
            data=request.data
            employee=self.serializer(data=data)

            if not employee.is_valid():
                return JsonResponse({'message':employee.error_messages},status=400)
            
            print(employee)
            employee.save()
            return JsonResponse({'employee': employee.data},status=200)
        except:
            return JsonResponse({'message':'error occured'},status=500)
        
        # do by query param
    def get(self,request):
        try:
            data=request.data
            employee=self.model.objects.filter(id=data['id'])
            json_data=self.serializer(employee,many=True)
        
            return JsonResponse({'employee':json_data.data},status=200)
        except:
            return JsonResponse({'message':'error occured'},status=500)
        
    def delete(self,request):
        try:
            data=request.data
            self.model.objects.filter(id=data['id']).delete()
            return JsonResponse({'message':'deleted successfully'},status=200)
        except:
            return JsonResponse({'message':'error occured'},status=500)


    def put(self,request):
        try:
            data=request.data
            instance=self.model.objects.get(id=data['id'])

            employee=self.serializer(instance=instance,data=data,partial=True)
            # print(employee)
            if not employee.is_valid():
                return JsonResponse({'message': employee.error_messages},status=400)

            employee.save()
            return JsonResponse({'message': employee.data},status=200)
        except:
            return JsonResponse({'message':'error occured'})


