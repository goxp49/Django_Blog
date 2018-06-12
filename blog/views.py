from django.shortcuts import render
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
    print(articles_all['articles_left'])
    return render(request, 'blog/index.html', {'articles_all': articles_all})