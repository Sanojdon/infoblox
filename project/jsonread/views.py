from django.http import HttpResponse
from django.template import loader

from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from jsonread.models import DataRead
from jsonread.serializers import DataReadSerializer


def index(request):
    template = loader.get_template('jsonread/index.html')
    context = {
        'name': "Sanoj Mathew",
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
class DataReadList(APIView):
    def get(self, request, format=None):
        data = DataRead.objects.all()
        serializer = DataReadSerializer(data, many=True)
        return Response(serializer.data)

class DataReadCreate(APIView):
    def post(self, request, format=None):
        serializer = DataReadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DataReadDetail(APIView):
    def get_object(self, pk):
        try:
            return DataRead.objects.get(dr_id=pk)
        except DataRead.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = DataReadSerializer(data)
        return Response(serializer.data)
