from django.contrib import admin
from MINI_TWITTER.models import User, Tweet
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)

admin.site.register(Tweet)

