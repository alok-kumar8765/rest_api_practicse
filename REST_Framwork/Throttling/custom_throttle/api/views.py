from .models import Students
from .serializers import StudentsSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle


class StudentsList(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'
    
class StudentsCreate(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

class StudentsRetrieve(RetrieveAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'

class StudentsUpdate(UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'modifystu'

class StudentsDestroy(DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    throttle_classes = [ScopedRateThrottle]