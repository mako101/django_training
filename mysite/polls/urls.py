from django.conf.urls import url

# . means current directory
from . import views

urlpatterns = [
    # 127.0.0.1/polls
    url('^$', views.index, name='index'),

    # 127.0.0.1/polls/1
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # 127.0.0.1/polls/1/results
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),

    # 127.0.0.1/polls/1/votes
    url(r'^(?P<question_id>[0-9]+)/votes$', views.vote, name='vote'),
        ]

