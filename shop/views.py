from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *


# Create your views here.
class CategoryApiView(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']
