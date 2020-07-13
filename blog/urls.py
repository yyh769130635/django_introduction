# Author:peter young
from django.contrib import admin
from django.urls import path
from blog import views
from django.conf.urls import url

urlpatterns = [
    url('^hello/$', views.index),
    url('^content/$', views.article_content),
    url(r'^index', views.get_index_page),
    # url('^detail/$', views.get_detail_page),
    path('detail/<int:article_id>/', views.get_detail_page),
]
