from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('poll/index.html')
    # template = loader.get_template('poll/index.html')


    return render(request,'poll/index.html',{'latest_question_list':latest_question_list})

def detail(request,question_id):
    return HttpResponse('You are looking at question %s.'%question_id)

def results(request, question_id):
    response = 'You are looking at the results question %s'
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse('You are voting on question %s'% question_id)

