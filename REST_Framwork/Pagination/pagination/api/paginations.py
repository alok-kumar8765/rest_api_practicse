from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination

class MyPagNumber(PageNumberPagination):
    page_size = 5
    page_query_param = 'p' #iska kam ye hai url me ?page=1 ko ?p=1 kr dega 
    page_size_query_param = 'record' #?p=1&record=10 mtlb 1 page pe 10 record show kre
    max_page_size = 5 #user 1 page pr max 5 data hi dekh skta h chahe kitni bar bhi record=7 ya 10 kre
    last_page_strings = 'end' #by default p=last hota h but ab humne end kr diya to yhi use hoga 

class MyLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'l'
    offset_query_param ='o'
    max_limit = 6 #ab chahe kuch bhi ho jae ek page pr 6 se jada data nhi dikhega
    
class MyCursourPagination(CursorPagination):
    page_size = 3
    ordering = 'name'
    cursor_query_param = 'page'