# Generated by Django 2.0.5 on 2018-06-20 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180620_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20, unique=True, verbose_name='分类名称')),
                ('category_describe', models.TextField(max_length=100, verbose_name='分类描述')),
                ('category_number', models.IntegerField(verbose_name='该分类文章数量')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Category', verbose_name='文章分类'),
        ),
    ]
