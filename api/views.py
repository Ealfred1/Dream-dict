from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import *

from .models import Dream
from .serializers import *


class Index(ListCreateAPIView):
  queryset = Dream.objects.all()
  serializer_class = DreamSerializer