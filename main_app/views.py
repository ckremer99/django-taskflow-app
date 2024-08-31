from django.shortcuts import render
from .models import Todo

def home(request):
    return render(request, 'home.html')

def todo_index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html/', { "todos": todos })

def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'todos/detail.html/', { "todo": todo })