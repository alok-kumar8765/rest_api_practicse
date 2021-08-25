from api_bacis.models import Article
from django.contrib import admin

# Register your models here.
#admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','author']