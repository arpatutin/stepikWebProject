# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by("-id")

    def popular(self):
        return self.order_by("-rating")


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=120)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name="question_like_user")

    def __str__(self):
        return self.title

    def get_url(self):
        return '/question/{}'.format(self.id)


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
