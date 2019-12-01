# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm


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
    if request.method == "GET":
        try:
            answers = Answer.objects.filter(question=quest)
        except:
            answers = []
        url = request.path
        return render(request, "question_template.html", {
            'question': quest,
            'answers': answers[:],
            'url': url
        })
    else:
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.add_question(quest=quest)
            form.save()
            return HttpResponseRedirect(request.path)


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            quest = form.save()
            url = quest.get_url()
            return HttpResponseRedirect(url)
    return render(request, 'askform.html')
