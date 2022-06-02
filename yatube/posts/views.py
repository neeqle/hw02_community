from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group
from .forms import PostForm
from datetime import datetime


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
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    paginator = Paginator(posts, 10)
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


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

def post_create(request):
    form = PostForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.user.is_authenticated:
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('posts:profile', request.user)
        return render(request, 'posts/create_post.html', context)
    else:
        return redirect('users:login')

def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', post.id)
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'posts/create_post.html', context)