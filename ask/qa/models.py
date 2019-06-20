# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):                                          
    def new(self):
        self.order_by("-added_at")
    def popular(self):
        self.order_by("-rating")

class Question(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.OneToOneField(User)
    likes = models.ManyToManyField(User, related_name="question_like_user")
    def __str__(self):
        return self.title
    def get_url(self):
        return '/question/{}'.format(self.id)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.OneToOneField(User)
