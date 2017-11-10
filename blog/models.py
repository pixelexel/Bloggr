# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.utils import timezone
from markdownx.models import MarkdownxField

class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length = 200)
    subtitle = models.CharField(max_length = 200, default = '')
    text = MarkdownxField() #extends Django's TextField and stores in DB accordingly
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def comments(self):
        return self.commentss

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
