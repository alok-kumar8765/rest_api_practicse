from api.models import Students
from django.shortcuts import render
from .serializers import StudentsSerializer
from rest_framework.generics import ListAPIView
from .models import Students
from rest_framework.filters import SearchFilter
# Create your views here.

class StudentsList(ListAPIView):
    #queryset = Students.objects.filter(passby = 'user1')
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    filter_backends = [SearchFilter]
    #search_fields = ['city']
    #search_fields = ['city','name']
    search_fields = ['^name'] # iska matlb ye hai jo bhi name ka pahla letter type 
                                #krke search krenge us letter wale sare name shoe honge
    
'''
super
pass- super

user1
pass-admin@123

user2
pass-admin@123

to use :- http://127.0.0.1:8000/stuapi/?search=ald
[^name] using :- http://127.0.0.1:8000/stuapi/?search=a
 age ?search ko change krke kuch aur krna hai to -->go to settings.py but ek bar change ho gya to search= ... kam nhi krega
 waps se default krna hoga
'''