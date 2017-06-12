#ncoding: utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^create/$', views.create, name='create'),
   url(r'^save/$', views.save, name='save'), 
   url(r'^edit/$', views.edit, name='edit'),
   url(r'^update/$', views.update, name='update'),
   url(r'^delete/$', views.delete, name='delete'),
]
