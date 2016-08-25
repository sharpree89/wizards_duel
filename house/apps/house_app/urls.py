from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^gryffindor$', views.gryffindor, name="gryffindor"),
    url(r'^hufflepuff$', views.hufflepuff, name="hufflepuff"),
    url(r'^ravenclaw$', views.ravenclaw, name="ravenclaw"),
    url(r'^slytherin$', views.slytherin, name="slytherin"),
]
