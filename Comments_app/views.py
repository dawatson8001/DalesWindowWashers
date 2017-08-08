# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import CommentPostForm


def post_list(request):

    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "Comments.html", {'posts': posts})


def new_post(request):
    form = CommentPostForm()
    return render(request, 'commentspostform.html', {'form': form})