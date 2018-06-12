from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=50,unique=True)
    article_describe = models.CharField(max_length=50)
    article_content = models.CharField(max_length=5000)
    article_cover = models.ImageField(upload_to='cover')
    article_ip = models.GenericIPAddressField()
    article_author = models.ForeignKey(get_user_model(),null=True,on_delete=models.SET_NULL)
    article_date = models.DateTimeField('last date of modify')
    article_hits = models.IntegerField()

    def __str__(self):
        return self.article_title

    def was_modify_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.article_date <= now

    was_modify_recently.admin_order_field = 'article_date'
    was_modify_recently.boolean = True
    was_modify_recently.short_description = 'Modify recently?'