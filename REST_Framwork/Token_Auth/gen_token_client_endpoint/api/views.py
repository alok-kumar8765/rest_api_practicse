
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
install httpie
now in terminal type :-
http POST http://127.0.0.1:8000/gettoken/ username="super" password="super"

you can custom your token response, create a auth.py
'''   