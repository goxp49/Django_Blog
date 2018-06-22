from django.contrib import admin
from .models import Article,Category,Message
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'article_author', 'article_category','article_date', 'article_hits')
    list_filter = ['article_author','article_date', 'article_category']
    search_fields = ['article_author']

    class Media:
        js = (
            '/static/blog/editor/kindeditor/kindeditor-all.js',#这是在后台的页面中追加js文件
            '/static/blog/editor/kindeditor/lang/zh-CN.js',
            '/static/blog/editor/kindeditor/config.js',
        )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_describe', 'category_number')
    list_filter = ['category_name']
    search_fields = ['category_name']

    class Media:
        js = (
            '/static/blog/editor/kindeditor/kindeditor-all.js',#这是在后台的页面中追加js文件
            '/static/blog/editor/kindeditor/lang/zh-CN.js',
            '/static/blog/editor/kindeditor/config.js',
        )

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'subject', 'email','date')
    list_filter = ['date']
    search_fields = ['sender']

    class Media:
        js = (
            '/static/blog/editor/kindeditor/kindeditor-all.js',#这是在后台的页面中追加js文件
            '/static/blog/editor/kindeditor/lang/zh-CN.js',
            '/static/blog/editor/kindeditor/config.js',
        )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Message, MessageAdmin)
#设定admin页面上的查看站点URL指向
admin.site.site_url = '/index'