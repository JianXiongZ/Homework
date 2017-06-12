# encoding: utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^$', views.login, name='login'),
   url(r'^validate_login/', views.validate_login, name='validate_login'),
   url(r'^list_name/', views.list_name, name='list_name'
       ),
   url(r'^create_user/', views.create_user, name='create_user'),
   url(r'^save_user/', views.save_user, name='save_user'),
   url(r'^update_user/', views.update_user, name='update_user'),
   url(r'^delete_user/', views.delete_user, name='delete_user'),
   url(r'^modify_update_user/', views.modify_update_user, name='modify_update_user')
]
