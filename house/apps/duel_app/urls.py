from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^lockhart$', views.lockhart, name="lockhart"),
    url(r'^process$', views.process, name='process'),
    url(r'^potter$', views.potter, name="potter"),
    url(r'^process_potter$', views.process_potter, name="process_potter"),
    url(r'^clear$', views.clear, name='clear'),
    url(r'^lose$', views.lose, name='lose'),
]
