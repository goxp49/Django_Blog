from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('single/<int:pk>/', views.single, name='single'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
]