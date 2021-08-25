'''
import re
from django.http import response
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import status
from rest_framework import viewsets

class StudentsViewSet(viewsets.ViewSet):
    def list(self,request):
        print('*********List**********')
        print('Basename:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('name:',self.name)
        print('Description:',self.description)
        stu = Students.objects.all()
        serializer = StudentsSerializer(stu,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        print('*********Retrieve**********')
        print('Basename:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('name:',self.name)
        print('Description:',self.description)
        id = pk
        if id is not None:
            stu = Students.objects.get(id = id)
            serializer = StudentsSerializer(stu)
            return Response(serializer.data)
    
    def create(self,request):
        print('*********Create**********')
        print('Basename:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('name:',self.name)
        print('Description:',self.description)
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        print('*********Update**********')
        print('Basename:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('name:',self.name)
        print('Description:',self.description)
        id = pk
        stu = Students.objects.get(pk=id)
        serializer = StudentsSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        print('*********Partial Update**********')
        print('Basename:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('name:',self.name)
        print('Description:',self.description)
        id = pk
        stu = Students.objects.get(pk=id)
        serializer = StudentsSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        print('*********Destroy**********')
        print('Basename:',self.basename)
        print('Action:',self.action)
        print('Detail:',self.detail)
        print('Suffix:',self.suffix)
        print('name:',self.name)
        print('Description:',self.description)
        id = pk
        stu = Students.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'},status=status.HTTP_200_OK)
    '''
    # Model View Set View
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import viewsets
    
class StudentsModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class StudentsReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer