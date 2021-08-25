
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api import views
from rest_framework.routers import DefaultRouter
'''
for function authntication url set
'''
# Creating Router Object
#router = DefaultRouter()

# Register Studentviwset with Router
#router.register('studentapi',views.StudentsModelViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include(router.urls)),#for class view
    #path('auth/',include('rest_framework.urls',namespace='rest_framework')),@for class view
    path('stuapi/',views.Student_api),
    path('stuapi/<int:pk>/',views.Student_api),
]
