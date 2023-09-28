from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'intro/intro_main.html')

def item(request, item_id, tab_id):
    if int(item_id) >= 10:
        url = "intro/item"+item_id+".html"
    elif int(item_id) < 10:
        url = "intro/item0"+item_id+".html"
    context = {'item_id':item_id,
               'tab_id':tab_id,}
    return render(request, url, context)

def map(request):
    return render(request, 'intro/intro_map.html')

def items(request):
    return render(request, 'intro/intro_items.html')

def video(request, item_id, video_id):
    if int(video_id) >= 10:
        url = "intro/video"+video_id+".html"
    elif int(video_id) < 10:
        url = "intro/video0"+video_id+".html"
    context = {'item_id':item_id,
               'video_id':video_id,}
    return render(request, url, context)