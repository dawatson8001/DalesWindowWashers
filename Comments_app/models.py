# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import getpass

from django.db import models
from django.utils import timezone
from DalesWindowWashers import settings

class Post(models.Model):

    class Meta:
        app_label = "Comments_app"

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    type = models.CharField(max_length=20, blank=True, null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.type