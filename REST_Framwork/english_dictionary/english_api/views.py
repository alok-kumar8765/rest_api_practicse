import re
from django.shortcuts import render
from rest_framework.utils import json
from rest_framework.views import View,APIView
from django.http import HttpResponse,JsonResponse
from .models import Word
from .serializers import WordSerializer
from rest_framework.decorators import api_view
from django.db.models.fields import IPAddressField

from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WordsSerializer
from rest_framework import status
# Create your views here.
@api_view(['GET'])
def WordList(request):
    if request.method == "GET":
        obj = Word.objects.all()
        Serializer = WordSerializer(obj,many=True)
        return Response(Serializer.data)


'''Using wordsserializer '''
#grabbing single obj from database
def WordsList(request,pk):
    obj=Word.objects.get(id=pk)#id of complex data 
    serializers = WordsSerializer(obj)#complex data convert into python
    #json_data = JSONRenderer().render(serializers.data)#python to json
    #return HttpResponse(json_data,content_type='application/json')#json data goes to client
    return JsonResponse(serializers.data,safe=False)

#get all data at once
def Word_detail(request):
    obj=Word.objects.all()#id of complex data 
    serializers = WordsSerializer(obj,many=True)#complex data convert into python
    json_data = JSONRenderer().render(serializers.data)#python to json
    return HttpResponse(json_data,content_type='application/json')#json data goes to client
    