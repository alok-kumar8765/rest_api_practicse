
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token #using to get token from terminal
from api.auth import CustomAuthToken
# Creating Router Object
router = DefaultRouter()

# Register Studentviwset with Router
router.register('studentapi',views.StudentsModelViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/',obtain_auth_token),
    path('token/',CustomAuthToken.as_view()),
]
