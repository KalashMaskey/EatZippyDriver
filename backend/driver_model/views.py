from django.shortcuts import render
from .serializers import DriverSerializers
from .models import DriverDetail
from rest_framework import viewsets
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """TEST API View"""

    def get(self,request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as functions (get,POST,put,Delete)',
            'Is similar to a traditional DjangoView',
            'Gives the most control over application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview': an_apiview})

class DriverView(viewsets.ModelViewSet):
    serializer_class = DriverSerializers
    queryset = DriverDetail.objects.all()
