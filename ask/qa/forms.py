from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=120)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
