from django.contrib import admin
from News.models import posts
from News.models import *
from News.models import News

# Register your models here.

admin.site.register(News)
admin.site.register(posts)

