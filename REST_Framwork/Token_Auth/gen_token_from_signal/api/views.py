
    # Model View Set View
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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

To use api with token, we do in terminal-
for GET use :- http http://127.0.0.1:8000/stuapi/ 'Authorization:Token fe569996e7256fd4800d0b747064256fa3152b2c'
for POST use :- http POST http://127.0.0.1:8000/stuapi/ name=shubham roll=6 city=saharanpu 'Authorization:Token fe569996e7256fd4800d0b747064256fa3152b2c'
for PUT use :- http PUT http://127.0.0.1:8000/stuapi/6/ name=rakesh roll=7 city=aligargh 'Authorization:Token fe569996e7256fd4800d0b747064256fa3152b2c'
for Delete use :- http POST http://127.0.0.1:8000/stuapi/4/  'Authorization:Token fe569996e7256fd4800d0b747064256fa3152b2c'
'''   