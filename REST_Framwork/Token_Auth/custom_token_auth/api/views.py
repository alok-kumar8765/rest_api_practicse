
    # Model View Set View
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import viewsets
from api.customauth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer    
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
'''
user= super
pass=super

To access after run server put http://127.0.0.1:8000/studentapi/?username=super
in url, ?username=username is required to login
'''