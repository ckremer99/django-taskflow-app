from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

class Home(LoginView):
    template_name = 'home.html'

def todo_index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html/', { "todos": todos })

def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'todos/detail.html/', { "todo": todo })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('todo-index')
        else: 
            error_message = 'Invalid signup - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
        



