from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model

# verbose_name 用于在admin界面中显示
class Article(models.Model):
    article_title = models.CharField(max_length=50,unique=True,verbose_name='文章标题')
    article_describe = models.TextField(max_length=50,verbose_name='文章描述')
    article_content = models.TextField(max_length=5000,verbose_name='文章内容')
    article_cover = models.ImageField(upload_to='cover',verbose_name='文章封面')
    article_ip = models.GenericIPAddressField(verbose_name='发布者IP地址')
    article_author = models.ForeignKey(get_user_model(),null=True,on_delete=models.SET_NULL,verbose_name='文章作者')
    article_category = models.ForeignKey('Category',null=True,on_delete=models.SET_NULL,verbose_name='文章分类')
    article_date = models.DateTimeField('最后修改日期')
    article_hits = models.IntegerField('点击量')

    def __str__(self):
        return self.article_title

    def was_modify_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.article_date <= now

    was_modify_recently.admin_order_field = 'article_date'
    was_modify_recently.boolean = True
    was_modify_recently.short_description = 'Modify recently?'

class Category(models.Model):
    category_name = models.CharField(max_length=20,unique=True,verbose_name='分类名称')
    category_describe = models.TextField(max_length=100,verbose_name='分类描述')
    category_number = models.IntegerField('该分类文章数量')

    def __str__(self):
        return self.category_name


class Message(models.Model):
    sender = models.CharField(max_length=20,unique=True,verbose_name='寄件人')
    subject = models.TextField(max_length=100,verbose_name='主题')
    message = models.TextField(max_length=1000,verbose_name='信息')
    email = models.EmailField(verbose_name='邮箱')
    date = models.DateTimeField(verbose_name='寄件日期')
    ipaddress = models.GenericIPAddressField(verbose_name='寄件人IP地址')

    def was_send_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now

    def __str__(self):
        return self.sender