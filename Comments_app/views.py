# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import CommentPostForm
from django.contrib.auth.decorators import login_required


def post_list(request):

    posts = Post.objects.order_by('-created_date')
    return render(request, "Comments.html", {'posts': posts})


@login_required(login_url='/login/')
def new_post(request):

    post = get_object_or_404(Post, pk=settings.AUTH_USER_MODEL)
    form = CommentPostForm()
    if request.method == "POST":
        comment_form = CommentPostForm(request.POST, instance=post)
        if comment_form.is_valid():
            comment = comment_form.save(False)
            comment.save()
    return render(request, 'commentspostform.html', {'form': form})