# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import CommentPostForm


def post_list(request):

    posts = Post.objects.order_by('-created_date')
    return render(request, "Comments.html", {'posts': posts})


def new_post(request):

    post = get_object_or_404(Post, pk=user_id)
    form = CommentPostForm()
    if request.method == "POST":
        comment_form = CommentPostForm(request.POST, instance=post)
        if comment_form.is_valid():
            comment = comment_form.save(False)
            comment.save()
    return render(request, 'commentspostform.html', {'form': form})