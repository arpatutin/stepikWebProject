# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from qa.models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')
def new(request):
    qs = Question.objects.new()
    limit = 10
    global page_int
    try:
        page_int = int(request.GET.get('page'))
    except:
        page_int = 1
    p = Paginator(qs, limit)
    p.baseurl = '/question/'
    try:
        page = p.page(page_int)
    except EmptyPage:
        return HttpResponseNotFound('Page id %s doesn\'t exit' % str(page_int))
    return render(request, 'new_template.html', {
        'paginator': p,
        'page': page
    })
def popular(request):
    qs = Question.objects.popular()
    limit = 10
    global page_int
    try:
        page_int = int(request.GET.get('page'))
    except:
        page_int = 1
    p = Paginator(qs, limit)
    p.baseurl = '/question/'
    try:
        page = p.page(page_int)
    except EmptyPage:
        return HttpResponseNotFound('Page id %s doesn\'t exit' % str(page_int))
    return render(request, 'popular_template.html', {
        'paginator': p,
        'page': page
    })
def question(request, id):
    try:
        quest = Question.objects.all()[int(qn)]
    except TypeError:
        return HttpResponseNotFound('')
    answers = Answer.objects.all()
    return render(request, "question_template.html", {
        'question': quest
        'range': range(0, len(answers))
        'answers': answers
    })


