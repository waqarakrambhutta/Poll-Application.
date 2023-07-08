from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from .models import Question,Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request,'poll/index.html',{'latest_question_list':latest_question_list})


def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'poll/detail.html',{'question':question})


def result(request, question_id):
    response = 'You are looking at the results question %s'
    return HttpResponse(response % question_id)


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