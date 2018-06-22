from django.shortcuts import render,get_object_or_404
from .models import Article,Message
from django.http import HttpResponse
# 引入创建的表单类
from .forms import ContactForm
import sys,os
sys.path.append("..")
from Django_Blog.settings import MEDIA_URL
import datetime
# Create your views here.

def index(request):
    articles_all = {}
    articles_left = []
    articles_mid = []
    articles_right = []
    articles_number = 0
    for article in Article.objects.exclude(article_category__category_name = '博客简介').all():
        articles_number += 1
        temp_dict = {}
        temp_dict['cover'] = str(article.article_cover)
        temp_dict['title'] = article.article_title
        temp_dict['describe'] = article.article_describe
        # 暂时使用id作为url----------------------------------------------------------
        temp_dict['url'] = article.id
        temp_dict['date'] = article.article_date
        if (articles_number % 3) == 1:
            articles_left.append(temp_dict)
        elif (articles_number % 3) == 2:
            articles_mid.append(temp_dict)
        elif (articles_number % 3) == 0:
            articles_right.append(temp_dict)
    articles_all['articles_left'] = articles_left
    articles_all['articles_mid'] = articles_mid
    articles_all['articles_right'] = articles_right
    #要通过dict的方式将参数传递给模板
    return render(request, 'blog/index.html', {'articles_all': articles_all})

def single(request,pk):
    article = {}
    article_db = get_object_or_404(Article, id=pk)
    #上方显示的文章主体
    article['title'] = article_db.article_title
    article['cover'] = str(article_db.article_cover)
    article['content'] = article_db.article_content
    article['author'] = article_db.article_author
    article['date'] = article_db.article_date
    #下方显示的其他文章
    #exclude为不等于括号中内容的结果
    #先给其他文章赋予默认图片和连接，搜索到正确数据后再覆盖
    article['other1_cover'] = article['other2_cover'] = article['other3_cover'] ='cover/NoArticle.jpg'
    article['other1_title'] = article['other2_title'] = article['other3_title'] ='快让博主多写几篇文章吧~~'
    article['other1_id'] = article['other2_id'] = article['other3_id'] = pk
    articles_number = 0
    for other_article in Article.objects.exclude(id = pk).exclude(article_category__category_name = '博客简介').order_by('?')[:3]:
        articles_number += 1
        if (articles_number % 3) == 1:
            article['other1_title'] = other_article.article_title
            article['other1_cover'] = other_article.article_cover
            article['other1_id'] = other_article.id
        elif (articles_number % 3) == 2:
            article['other2_title'] = other_article.article_title
            article['other2_cover'] = other_article.article_cover
            article['other2_id'] = other_article.id
        elif (articles_number % 3) == 0:
            article['other3_title'] = other_article.article_title
            article['other3_cover'] = other_article.article_cover
            article['other3_id'] = other_article.id
    return render(request, 'blog/single.html',{'article': article})

def blog(request):
    articles_all = {}
    articles_left = []
    articles_mid = []
    articles_right = []
    articles_number = 0
    for article in Article.objects.exclude(article_category__category_name = '博客简介').all():
        articles_number += 1
        temp_dict = {}
        temp_dict['cover'] = str(article.article_cover)
        temp_dict['title'] = article.article_title
        temp_dict['describe'] = article.article_describe
        # 暂时使用id作为url----------------------------------------------------------
        temp_dict['url'] = article.id
        temp_dict['date'] = article.article_date
        if (articles_number % 3) == 1:
            articles_left.append(temp_dict)
        elif (articles_number % 3) == 2:
            articles_mid.append(temp_dict)
        elif (articles_number % 3) == 0:
            articles_right.append(temp_dict)
    articles_all['articles_left'] = articles_left
    articles_all['articles_mid'] = articles_mid
    articles_all['articles_right'] = articles_right
    #要通过dict的方式将参数传递给模板
    return render(request, 'blog/blog.html', {'articles_all': articles_all})

def about(request):
    article = {}
    article_db = get_object_or_404(Article,article_category__category_name = '博客简介')
    #上方显示的文章主体
    article['title'] = article_db.article_title
    article['cover'] = str(article_db.article_cover)
    article['content'] = article_db.article_content
    article['author'] = article_db.article_author
    article['date'] = article_db.article_date
    #下方显示的其他文章
    #exclude为不等于括号中内容的结果
    #先给其他文章赋予默认图片和连接，搜索到正确数据后再覆盖
    article['other1_cover'] = article['other2_cover'] = article['other3_cover'] ='cover/NoArticle.jpg'
    article['other1_title'] = article['other2_title'] = article['other3_title'] ='快让博主多写几篇文章吧~~'
    article['other1_id'] = article['other2_id'] = article['other3_id'] = article_db.id
    articles_number = 0
    for other_article in Article.objects.exclude(id = article_db.id).exclude(article_category__category_name = '博客简介').order_by('?')[:3]:
        articles_number += 1
        if (articles_number % 3) == 1:
            article['other1_title'] = other_article.article_title
            article['other1_cover'] = other_article.article_cover
            article['other1_id'] = other_article.id
        elif (articles_number % 3) == 2:
            article['other2_title'] = other_article.article_title
            article['other2_cover'] = other_article.article_cover
            article['other2_id'] = other_article.id
        elif (articles_number % 3) == 0:
            article['other3_title'] = other_article.article_title
            article['other3_cover'] = other_article.article_cover
            article['other3_id'] = other_article.id
    return render(request, 'blog/single.html',{'article': article})

def contact(request):
    if request.method == 'POST':# 当提交表单时
        form = ContactForm(request.POST)    # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            sender_address = form.cleaned_data['sender_address']
            #如果使用代理服务器时也能或得到正确的IP地址
            try:
                ip = request.META['HTTP_X_FORWARDED_FOR']
            except:
                ip = request.META['REMOTE_ADDR']

            try:
                Message.objects.create(sender=name, subject=subject, message=message, email=email, sender_address=sender_address,
                                       ipaddress=ip)
            except:
                HttpResponse("服务器正忙，请稍后再试~")
    elif request.method == 'GET':# 当正常访问时
        pass
    return render(request, 'blog/contact.html')
