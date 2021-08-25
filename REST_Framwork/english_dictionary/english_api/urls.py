from django.urls import path
from django.urls.resolvers import URLPattern
from .views import WordList
from . import views


urlpatterns = [
    path('words/',views.WordList,name='word_list'),
]
