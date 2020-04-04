from django.shortcuts import render, get_object_or_404
from .models import Post, Group

def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})

def group_posts(request, slug):
    # функция get_object_or_404 получает по заданным критериям объект из базы данных 
    # или возвращант сообщение об ошибке, если объект не найден
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
# Create your views here.
