from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^create$', views.create),
    url(r'^show_all$', views.show_all),
    url(r'^manage$', views.manage),
    url(r'^view/(?P<issue_id>\d+)$', views.view),
    url(r'^edit/(?P<issue_id>\d+)$', views.edit),
    url(r'^createNew$', views.createNew),
    url(r'^update$', views.update),
]