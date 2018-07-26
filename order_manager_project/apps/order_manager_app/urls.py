from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^create$', views.create),
    url(r'^show_all$', views.show_all),
    url(r'^manage$', views.manage),
    url(r'^view$', views.view),
    url(r'^edit$', views.edit),
]