import re
from django.http import response
from django.shortcuts import render
from requests import api
from rest_framework import serializers
from rest_framework.decorators import APIView, api_view #used for function based api view
from rest_framework.response import Response
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.views import APIView #for class view
from rest_framework import status
'''
the below file/moodules use for generic & mixins
'''
from .models import Students
from .serializers import StudentsSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, CreateModelMixin,RetrieveModelMixin, UpdateModelMixin
# Create your views here.

#@api_view(['GET'])
#def hello_world(request):
    #return Response({'msg':'hello world'})

#@api_view(['POST'])
#def hello_world(request):
    #if request.method == 'POST':
        #print(request.data)
        #return Response({'msg':'This is POST Request'})
'''
#function based APIView        
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def Student_api(request,pk=None):
    if request.method == "GET":
        #id = request.data.get('id') #when pk is not intialized in function
        id = pk
        if id is not None:
            stu = Students.objects.get(id=id)
            serializers = StudentsSerializer(stu)
            return Response(serializers.data)
        stu = Students.objects.all()
        serializers = StudentsSerializer(stu, many=True)
        return Response(serializers.data)
    
    if request.method == 'POST':
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        #id = request.data.get('id')
        id = pk
        stu = Students.objects.get(pk=id)
        serializer = StudentsSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        #id = request.data.get('id')
        id = pk
        stu = Students.objects.get(pk=id)
        serializer = StudentsSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Prtial Data Updated'})
        return Response(serializer.errors)
    
    
    if request.method == 'DELETE':
        #id = request.data.get('id')
        id = pk
        stu = Students.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
'''
'''
# Class based APIView
class Student_Api(APIView):
    def get(self,request,pk=None,format=None):
        id = pk
        if id is not None:
            stu = Students.objects.get(id=id)
            serializers = StudentsSerializer(stu)
            return Response(serializers.data)
        stu = Students.objects.all()
        serializers = StudentsSerializer(stu, many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk,format=None):
        id = pk
        stu = Students.objects.get(pk=id)
        serializer = StudentsSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors)
    
    def patch(self,request,pk,format=None):
        id = pk
        stu = Students.objects.get(pk=id)
        serializer = StudentsSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Prtial Data Updated'})
        return Response(serializer.errors)
    def delete(self,request,pk,format=None):
        id = pk
        stu = Students.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
'''
'''
#list model mixins individual functions of CURD
class StudentsList(GenericAPIView,ListModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args,**kwargs)
 #only create will work   
class StudentsCreate(GenericAPIView,CreateModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args,**kwargs)
# only retive
class StudentsRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
'''

#Group-by mixin list and creat in same class because pk not required
class LCStudentsAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
#Group by retrieve, update, destroy pk is required
class RUDStudentsAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)