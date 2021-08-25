
from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/',views.StudentsList.as_view()),
    path('stuapi/<int:pk>/',views.StudentsRetrieve.as_view()),
    #path('postapi/',views.StudentsCreate.as_view()),
    path('updateapi/<int:pk>/',views.StudentsUpdate.as_view()),
    path('deleteapi/<int:pk>/',views.StudentsDestroy.as_view()),
]
