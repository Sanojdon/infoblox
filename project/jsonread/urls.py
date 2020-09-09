from django.urls import path
from django.conf.urls import include, re_path
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework.urlpatterns import format_suffix_patterns

from jsonread import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/all', views.DataReadList.as_view()),
    path('api/<int:pk>', views.DataReadDetail.as_view()),
    path('api/new', views.DataReadCreate.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
