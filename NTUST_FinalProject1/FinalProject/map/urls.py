from django.conf.urls import url
from django.contrib.auth.views import (login, logout)
from . import views

urlpatterns = [
    url(r'^$', views.photo_list, name='photo_list'),
    #url(r'^record/$', views.record, name='record'),
    url(r'^diary/$',views.diary, name='diary'),
    url(r'^Diary_Page/$',views.Diary_Page, name='Diary_Page'),
    url(r'^$', views.home),
	url(r'^Login_Page/$', login, {'template_name': 'map/Login_Page.html'}, name='Login_Page'),
	url(r'^logout/$', logout, {'template_name': 'map/logout.html'}, name='logout'),
	url(r'^diary/$', login, {'template_name': 'map/diary.html'}, name='diary'),
	url(r'^Register_Page/$', views.register, name='Register_Page'),
]
