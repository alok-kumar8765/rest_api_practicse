
    # Model View Set View
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class StudentsModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer    
    '''
    when auth used globally
    '''
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    #permission_classes = [AllowAny]
    #permission_classes = [IsAdminUser] #Only user can excees if it's staff status is ok/true/checked no t=other can axcess
    '''
    if we create user under super user they can have rights 
    to CURDS fuction like super user. All they need to be  authentiated in 
    basic authentication, there will be no ristrictions.
    user's  user-alok
            pass-alok.8765
    Admin's user-admin_local
            pass-super8765
    super   user-admin
            pass-admin
    
    If we have lager number of class then either we can use auth and 
    permission to every class or we globally use, for that go to settings.py and end
    mention
    '''