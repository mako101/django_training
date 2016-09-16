from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^browse$', views.browse, name='browse'),
    url(r'^upload/submit$', views.submit, name='submit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
