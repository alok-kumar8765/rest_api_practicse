from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns = [
    path('product/',views.product_list),
    path('product/<int:pk>/',views.product_detail),
]
