from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from .paginations import MyPagNumber,MyLimitOffSetPagination, MyCursourPagination
# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #pagination_class = MyPagNumber
    #pagination_class = MyLimitOffSetPagination
    pagination_class = MyCursourPagination

'''
For global setting of pagination go to setting.py,
when you using limitoff set :-  http://127.0.0.1:8000/stuapi/?l=2&o=6 
here ?l=2 means limit lga diya ek page par bas 2 data dikhe aur o=6 means offset (6 number se age ka data dikhe)

CursourPagination :- as we don't use time stamp there will be error shown as keyword "created", isko
                    override krne ke liye pagination.py me, ordering = "name" se kiya, mtlb ab jo bhi show ho
                    name ke basis pe,alphabatically, hum chahe to city ya roll kisi ek se bhi kr skte hai. 
'''