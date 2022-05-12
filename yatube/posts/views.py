
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

POSTS_COUNT = 10


def index(request):
    posts = Post.objects.all()[:POSTS_COUNT]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_COUNT]
    title = 'Записи группы'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)
