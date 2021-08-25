
    # Model View Set View
from .models import Students
from .serializers import StudentsSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from api.throttlings import SetThrottle

class StudentsModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer    
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle,SetThrottle]
'''
super user-super
      pass-super
throttling ke help se unknown ya authenticated person ko kitne bar api request
ho set krte hai, 
yha unknown user 1 din me 2 bar aur authntic user 5 bar api open(get/post ect)
kr skta h jisko settings.py me last me set kiya hai.

ab agar bhut sare class ho sb pe alg alg times set krna ho to throttling.py page pe 
coding hai.

'''   