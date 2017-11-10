# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, SignUpForm
from .models import Post, Comment
#Sign Up
from django.contrib.auth import login, authenticate
from markdownx.utils import markdownify

# Create your views here.

def index(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html', {'posts' : posts})

def about(request):
    return render(request, 'blog/about.html', {})

def contact(request):
    return render(request, 'blog/contact.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.publish()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form' : form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if(request.user == post.author):
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if(request.user == post.author):
        post.delete()
    return user_detail(request, request.user) #instead of rendering a new view, just call the user_detail view

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date') #lte => less than or equal to
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.text = markdownify(post.text)
    return render(request, 'blog/post_detail.html', {'post' : post})

def user_detail(request, user):
    posts = Post.objects.filter(published_date__lte = timezone.now(),  author__username = user).order_by('-published_date') #To access foreign key relations use key__attribute # User is a string like author__username so only that can be compared!
    return render(request, 'blog/user_detail.html', {'posts' : posts, 'username' : user})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})
