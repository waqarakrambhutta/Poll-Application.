from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request,'poll/index.html',{'latest_question_list':latest_question_list})

def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    return render(request,'poll/detail.html',{'question':question})

def results(request, question_id):
    response = 'You are looking at the results question %s'
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse('You are voting on question %s'% question_id)

