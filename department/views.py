from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from .models import *
from .serializer import *

# Create your views here.
class DepartmentView(generics.GenericAPIView):
    model=Department
    serializer=DepartmentSerializer

    def post(self,request):
        try:
            data=request.data
            department=self.serializer(data=data)

            if not department.is_valid():
                return JsonResponse({'message': department.error_messages},status=400)
            
            # print(department)
            department.save()
            return JsonResponse({'message':department.data})
        except:
            return JsonResponse({'message':'error occured'},status=500)
        
    def delete(self,request):
        try:
            data=request.data
            self.model.objects.get(id=data['id']).delete()
            return JsonResponse({'message':'deleted successfully'},status=204)
        except:
            return JsonResponse({'message':'error occured'},status=500)
        
    def get(self,request):
        try:
            data=request.data
            department=self.model.objects.filter(id=data['id'])
            json_data=self.serializer(department,many=True)
            # print(json_data)
            return JsonResponse({'message':json_data.data},status=200)
        
        except:
            return JsonResponse({'message':'error occured'},status=500)
        
    def put(self,request):
        try:
            data=request.data
            instance=self.model.objects.get(pk=data['id'])
            department=self.serializer(instance=instance,data=data,partial=True)
            # print(department.data)
            if not department.is_valid():
                return JsonResponse({'message': department.error_messages},status=400)
            
            department.save()

            return JsonResponse({'department': department.data})
        except:
            return JsonResponse({'message':'error occured'},status=500)