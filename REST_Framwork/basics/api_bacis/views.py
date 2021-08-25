from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        print(articles)
        serializer = ArticleSerializer(articles,many=True)
        print(serializer)
        json_data = JSONRenderer().render(serializer.data)
        return JsonResponse(serializer.data,safe=False)
        return HttpResponse(json_data, content_type='application/json')
   
    #safe=False is defined here because serialized data is not in dictionary... If the serialized data is in dict than there is no need to define safe=False
    elif request.model == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors,status=400)