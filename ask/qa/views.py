# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from qa.models import Question, Answer


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
    return render(request, 'pagination_template.html', {
        'paginator': p,
        'page': page
    })


def popular(request):
    qs = Question.objects.popular()
    limit = 10
    paging = 1
    try:
        paging = int(request.GET.get('page'))
    except:
        paging = 1
    p = Paginator(qs, limit)
    p.baseurl = '/question/'
    try:
        page = p.page(paging)
    except EmptyPage:
        return HttpResponseNotFound('Page id %s doesn\'t exit' % str(paging))
    return render(request, 'pagination_template.html', {
        'paginator': p,
        'page': page
    })


def question(request, idem):
    try:
        quest = Question.objects.all()[int(idem)]
    except TypeError:
        return HttpResponseNotFound('')
    answers = Answer.objects.filter(question=idem)
    return render(request, "question_template.html", {
        'question': quest,
        'answers': answers[:]
    })
