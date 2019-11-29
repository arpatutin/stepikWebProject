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
    paging = request.GET.get('page', 1)
    p = Paginator(qs, limit)
    p.baseurl = '/question/'
    try:
        page = p.page(paging)
    except EmptyPage:
        return HttpResponseNotFound('Page id %s doesn\'t exit' % str(paging))
    return render(request, 'pagination_template.html', {
        'paginator': p,
        'page': page,
        'objects': page.object_list[:]
    })


def popular(request):
    qs = Question.objects.popular()
    limit = 10
    paging = request.GET.get('page', 1)
    p = Paginator(qs, limit)
    p.baseurl = '/question/'
    try:
        page = p.page(paging)
    except EmptyPage:
        return HttpResponseNotFound('Page id %s doesn\'t exit' % str(paging))
    return render(request, 'pagination_template.html', {
        'paginator': p,
        'page': page,
        'objects': page.object_list[:]
    })


def question(request, idem):
    quest = get_object_or_404(Question, id=idem)
    answers = Answer.objects.get(question=quest)
    return render(request, "question_template.html", {
        'question': quest,
        'answers': answers[:]
    })
