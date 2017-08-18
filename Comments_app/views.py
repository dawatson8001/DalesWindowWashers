# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentPostForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def post_user_list(request):

    posts = Post.objects.order_by('-created_date')
    return render(request, "usercomments", {'posts': posts})


def post_list(request):

    posts = Post.objects.order_by('-created_date')
    return render(request, "comments.html", {'posts': posts})


@login_required
def new_comment(request):
    if request.method == "POST":
        form = CommentPostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.user = request.user
            post.save()
            return redirect(post_list)
    else:
        form = CommentPostForm()
    return render(request, 'newcomment.html', {'form': form})


@login_required
def edit_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect(post_user_list)
    else:
        form = CommentPostForm(instance=post)
    return render(request, 'usercommentedit.html', {'form': form})


@login_required
def delete_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()

    return redirect(post_user_list)