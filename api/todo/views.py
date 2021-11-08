from django.shortcuts import render
from models import Todo
from serializers import TodoSerializer
# Create your views here.

class TodiViewset(viewsets.ModelViewset):
    #use all the objects that are Todo
    queryset = Todo.objects.all()
    serializers_class = TodoSerializer