from django.conf.urls import url
from . import views
from django.contrib.auth.views import (login, logout)
from map.views import HomeView

urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/$', login, {'template_name': 'map/login.html'}, name='login'),
	url(r'^logout/$', logout, {'template_name': 'map/logout.html'}, name='logout'),
	url(r'^diary/$', login, {'template_name': 'map/diary.html'}, name='diary'),
	url(r'^register/$', views.register, name='register'),
	url(r'^add/$', HomeView.as_view(), name='add'),
]