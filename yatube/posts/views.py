from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group

POSTS_COUNT = 10


def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context) 


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:POSTS_COUNT]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
