from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from datetime import datetime

# POSTS_COUNT = 10


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': post_list,
        'year' : datetime.now().year,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context) 


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    # posts = group.posts.all()[:POSTS_COUNT]
    paginator = Paginator(posts, 10)
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)


def profile(request, username):
    posts = Post.objects.filter(author__username=username)
    post_count = posts.count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'post_count': post_count,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    posts = Post.objects.filter(pk=post_id)
    context = {
        'posts': posts,
    }
    return render(request, 'posts/post_detail.html', context)