from django.conf.urls import url

# . means current directory
from . import views

# Have to be careful with app_name, this allows to change the app's namespace!
# It also doesn't seem to be needed? -> Check with Maddy
#app_name = 'surveys'
app_name = 'polls'

urlpatterns = [
    # 127.0.0.1/polls
    url(r'^$', views.index, name='index'),

    # 127.0.0.1/polls/1
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # # if we call this url by name, we jst need to change it here
    # # without updating the templates, and the new URL will work!
    # # 127.0.0.1/polls/question/1
    # url(r'^question/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # 127.0.0.1/polls/1/results
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),

    # 127.0.0.1/polls/1/vote
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote'),
        ]

