"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from lists import views

urlpatterns = [
    '''
    lists/new will be the same for every user, a blank list that they fill out
    once the first item is entered, they are redirected to the url of their list's id
    in the database. Here we pass the id to the views.py file with a captured regex.
    To add new items to this existing list, they are redirected to lists/list_id/add_item.
    '''
    url(r'^$', views.home_page, name="home"),
    url(r'^lists/new$', 'lists.views.new_list', name='new_list'),
    url(r'^lists/(\d+)/$', 'lists.views.view_list', name='view_list'),
    url(r'^lists/(\d+)/add_item$', views.add_item, name='add_item'),
    # url(r'^admin/', include(admin.site.urls)),
]

