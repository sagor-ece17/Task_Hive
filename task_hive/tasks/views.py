from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Task

def index(request):
    tasks = Task.objects.all()

    context = {'tasks' : tasks}
    return render(request, 'tasks.html', context)
