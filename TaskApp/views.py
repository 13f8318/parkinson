from django.shortcuts import render
from .models import Task
from rest_framework import viewsets
from .Serializers import TaskSerializers

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers

class DueTaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
    serializer_class = TaskSerializers

class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
    serializer_class = TaskSerializers