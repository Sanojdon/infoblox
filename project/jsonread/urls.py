from django.urls import path
from django.conf.urls import include, re_path
# from rest_framework.urlpatterns import format_suffix_patterns

from jsonread import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/all', views.DataReadList.as_view()),
    path('api/<int:pk>', views.DataReadDetail.as_view()),
    path('api/new', views.DataReadCreate.as_view()),
]
