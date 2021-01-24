"""Defines URL patterns for cypher_app."""

from django.urls import path

from . import views

app_name = 'cypher_app'
urlpatterns = [
	# Home
	path('', views.index, name='index'),

	# Cipher Pages
	path('app', views.app, name='app'),
	path('others', views.others, name='others'),
]