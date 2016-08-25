from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^lockhart$', views.lockhart, name="lockhart"),
    url(r'^process$', views.process, name='process'),
    url(r'^clear$', views.clear, name='clear'),
]
