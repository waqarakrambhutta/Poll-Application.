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


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,
               'poll/detail.html',
               {
                   'question':question,
                   'error_message':"You didn't select a choice."
               }
               )

    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:result',args=(question_id)))