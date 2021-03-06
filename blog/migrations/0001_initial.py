# Generated by Django 2.0.5 on 2018-06-11 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=50, unique=True)),
                ('article_describe', models.CharField(max_length=50)),
                ('article_content', models.CharField(max_length=5000)),
                ('article_cover', models.ImageField(upload_to='cover')),
                ('article_ip', models.GenericIPAddressField()),
                ('article_date', models.DateTimeField(verbose_name='last date of modify')),
                ('article_hits', models.IntegerField()),
                ('article_author', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
