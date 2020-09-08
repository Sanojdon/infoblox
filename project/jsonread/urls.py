from django.urls import path
from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from jsonread.views import DataReadViewSet

from . import views

router = DefaultRouter()
router.register("api",DataReadViewSet)


urlpatterns = [
    # path('', views.index, name='index'),
    re_path('^', include(router.urls)),
]
