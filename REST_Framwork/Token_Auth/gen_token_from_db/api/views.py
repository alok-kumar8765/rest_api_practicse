
    # Model View Set View
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer    
    #authentication_classes = [SessionAuthentication]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
'''
super user-super
      pass-super
user's user-user1
       pass- admin@123
      
we are simply generate 
token method1:-  
db me ja kar,token tables open krke add tokens click krna hai,db me jitne users hai
drop down me show krega, jisko token provide krna hai use select kr dena. 
method 2:- using terminal
python manage.py drf_create_token user1(yha jis user ka token gen krna uska name aur wo user name db me ho)
'''   