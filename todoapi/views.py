from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializers import TodoSerializer
from .models import Todo


class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
