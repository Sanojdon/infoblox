from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

from jsonread.models import DataRead
from .serializers import DataReadSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the JSON index.")

# Create your views here.

class DataReadViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
    serializer_class = DataReadSerializer
    queryset = DataRead.objects.all()
