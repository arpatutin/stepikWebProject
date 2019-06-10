# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.OneToOneField(User)
    likes = [models.OneToOneField(User)]
class QuestionManager(models.Manager):                                          
    def new():                                                              
            pass                                                            
    def popular():                                                          
            pass 
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question)
    author = models.OneToOneField(User)

