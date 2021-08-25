import re
from rest_framework import serializers
from api_one.models import Student
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Model Object- single  student data
def student_details(request,insrt_url):
    stu=Student.objects.get(id=insrt_url)
    #print(stu)
    serializer=StudentSerializer(stu)
    #print(serializer)
    #print(serializer.data)
    #json_data= JSONRenderer().render(serializer.data)
    #print(json_data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)
    
#   Queryset
def student_list(request):
    stu=Student.objects.all()
    #print(stu)
    serializer=StudentSerializer(stu, many=True)
    #print(serializer)
    #print(serializer.data)
   # json_data= JSONRenderer().render(serializer.data)
    #print(json_data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)
