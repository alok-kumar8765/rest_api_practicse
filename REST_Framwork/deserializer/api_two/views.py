import json
from django.shortcuts import render
import io
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re
from rest_framework.utils import json
from rest_framework.views import View,APIView
from rest_framework.decorators import api_view
from django.db.models.fields import IPAddressField
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream= io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is save'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
    json_data=JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data,content_type='application/json') 