from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    welcome_msg = '<h3>Welcome to the polls app!</h3><h5>Here are the latest questions:</h5>'
    output = '<br>'.join(q.question_text for q in latest_questions)
    # return HttpResponse('<h1>Hello and welcome. You\'re at the polls index.<h1>')
    return HttpResponse(welcome_msg + output)

def detail(request, question_id):
    return HttpResponse('This is the detail view of the question is: %s' % question_id)


def results(request, question_id):
    return HttpResponse('These are the results of the questions: %s' % question_id)

def votes(request, question_id):
    return HttpResponse('The vote on question is: %s' % question_id)