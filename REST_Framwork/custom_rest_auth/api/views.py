#Function Baed Auth and Permission
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import status
    # Class Custom Aut Permission View Set View
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,BaseAuthentication, SessionAuthentication
from .custompermission import MyPermission

#class StudentsModelViewSet(viewsets.ModelViewSet):
    #queryset = Students.objects.all()
    #serializer_class = StudentsSerializer  
    #authentication_classes = [SessionAuthentication]
    #permission_classes = [MyPermission]  
'''
    user's  user-alok
            pass-alok.8765
    Admin's user-admin_local
            pass-super8765
    super   user-admin
            pass-admin
    
'''
# Function based 
@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
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