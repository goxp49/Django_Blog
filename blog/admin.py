from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'article_author', 'article_date', 'article_hits')
    list_filter = ['article_author','article_date']
    search_fields = ['article_author']

admin.site.register(Article, ArticleAdmin)
#设定admin页面上的查看站点URL指向
admin.site.site_url = '/index'