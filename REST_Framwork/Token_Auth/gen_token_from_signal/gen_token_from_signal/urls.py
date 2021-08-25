
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api import views
from rest_framework.routers import DefaultRouter
# Creating Router Object
router = DefaultRouter()

# Register Studentviwset with Router
router.register('stuapi',views.StudentsModelViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    
]
