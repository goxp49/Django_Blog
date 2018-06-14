from django.shortcuts import render,get_object_or_404
from .models import Article
# Create your views here.

def index(request):
    articles_all = {}
    articles_left = []
    articles_mid = []
    articles_right = []
    articles_number = 0
    for article in Article.objects.all():
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
    articles_number = 0
    for other_article in Article.objects.exclude(id = pk).order_by('?')[:2]:
        articles_number += 1
        if (articles_number % 3) == 1:
            article['other1_title'] = other_article.article_title
            article['other1_cover'] = other_article.article_cover
        elif (articles_number % 3) == 2:
            article['other2_title'] = other_article.article_title
            article['other2_cover'] = other_article.article_cover
        elif (articles_number % 3) == 0:
            article['other3_title'] = other_article.article_title
            article['other3_cover'] = other_article.article_cover
    return render(request, 'blog/single.html',{'article': article})