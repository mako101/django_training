from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from django.shortcuts import render, Http404, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Question
# Create your views here.

def index(request):
    latest_questions = Question.objects.order_by('pub_date')[:5]

    # # The long version!!
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_questions': latest_questions
    # }
    # return HttpResponse(template.render(context, request))

    # The short version! - using the 'render'shortcut
    context = {'latest_questions': latest_questions}
    # here is the right order of arguments for the render function
    return render(request, 'polls/index.html', context)

    # Playing around
    # welcome_msg = '<h3>Welcome to the polls app!</h3><h5>Here are the latest questions:</h5>'
    # output = '<br>'.join(q.question_text for q in latest_questions)
    # return HttpResponse('<h1>Hello and welcome. You\'re at the polls index.<h1>')


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("The question with ID {} does not exist".format(question_id))
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
            return render(request, 'polls/detail.html', {'question': question, 'error_message': 'Please select one of the available choices'})
    else:
        selected_choice.votes += 1
        selected_choice.save()

    # must have a comma if you pass just one argument
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

