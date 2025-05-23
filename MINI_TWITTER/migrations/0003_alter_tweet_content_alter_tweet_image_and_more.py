# Generated by Django 5.1.2 on 2024-10-27 20:10

import django.contrib.auth.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MINI_TWITTER', '0002_user_followers_alter_user_email_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(blank=True, max_length=280, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tweets'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='liked_by',
            field=models.ManyToManyField(blank=True, default=0, related_name='liked_tweets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
