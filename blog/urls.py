"""blog URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]