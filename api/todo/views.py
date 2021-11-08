from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.

class TodoViewset(viewsets.ModelViewSet):
    #use all the objects that are Todo
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer