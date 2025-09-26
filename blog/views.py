from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Author


def home(request):
    """Home page showing recent posts"""
    posts = Post.objects.filter(published=True).select_related('author').order_by('-created_at')[:5]
    return render(request, 'blog/home.html', {'posts': posts})


def post_list(request):
    """List all published posts"""
    posts = Post.objects.filter(published=True).select_related('author').order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    """Show individual post details"""
    post = get_object_or_404(Post, id=post_id, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})


def author_list(request):
    """List all authors"""
    authors = Author.objects.all().order_by('user__first_name', 'user__last_name')
    return render(request, 'blog/author_list.html', {'authors': authors})


def author_detail(request, author_id):
    """Show individual author details and their posts"""
    author = get_object_or_404(Author, id=author_id)
    posts = Post.objects.filter(author=author, published=True).order_by('-created_at')
    return render(request, 'blog/author_detail.html', {'author': author, 'posts': posts})
