# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentPostForm
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse


def post_user_list(request):

    posts = Post.objects.order_by('-created_date')
    return render(request, "usercomments", {'posts': posts})


def post_list(request):

    posts = Post.objects.order_by('-created_date')
    return render(request, "comments.html", {'posts': posts})


@login_required
def new_post(request):

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
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = CommentPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(post_list)
    else:
        form = CommentPostForm(instance=post)

    args = {
        'form': form,
        'form_action': reverse('edit_post', kwargs={"post_id": post.id})
    }
    args.update(csrf(request))
    return redirect(post_list)