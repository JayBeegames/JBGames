from django.shortcuts import render
from django.shortcuts import render_to_response
from News.models import News

from News.models import posts

# Create your views here.

def home(request):
    entries = posts.objects.all()[:10]
    return render_to_response('index.html', {'posts' : entries})

def newspage(request):
    return render_to_response('news.html')
