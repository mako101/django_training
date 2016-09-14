from django.conf.urls import url

# . means current directory
from . import views

urlpatterns = [
    # 127.0.0.1/
    url('^$', views.root_index, name='index')
    ]