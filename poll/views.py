from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Question,Choice


# Create your views here.
class IndexView(generic.ListView):
    template_name='poll/index.html'
    context_object_name='latest_object_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name='poll/detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'


class VoteView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'