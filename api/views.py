from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer
# from django.http import HttpResponse

# Create your views and api endpoints here.

#MAIN API VIEW
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer 

# #MAIN HTML VIEW
# def main(request):
#     return HttpResponse("<h1>Hello</h1>")


