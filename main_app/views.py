from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Todo, Flag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import TodoForm, CompletedForm

class Home(LoginView):
    template_name = 'home.html'

def todo_index(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/index.html/', { "todos": todos })

def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    flags_todo_doesnt_have = Flag.objects.exclude(id__in = todo.flags.all().values_list('id'))
    flags = todo.flags.all()
    completed_form = CompletedForm(instance=todo)
    return render(request, 'todos/detail.html', {
         'todo': todo,
         'flags_todo_doesnt_have': flags_todo_doesnt_have,
         'flags': flags,
         'completed_form': completed_form,
    })

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

def associate_flag(request, todo_id, flag_id):
    Todo.objects.get(id=todo_id).flags.add(flag_id)
    return redirect('todo-detail', todo_id=todo_id)

def remove_flag(request, todo_id, flag_id):
    Todo.objects.get(id=todo_id).flags.remove(flag_id)
    return redirect('todo-detail', todo_id=todo_id)

def update_completed(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo-detail', todo_id=todo_id)
        
class TodoCreate(CreateView):
    model = Todo
    form_class = TodoForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm

class TodoDelete(DeleteView):
    model = Todo
    success_url = '/todos/'

class FlagCreate(CreateView): 
    model = Flag
    fields = '__all__' 

class FlagList(ListView):
    model = Flag

class FlagDetail(DetailView):
    model = Flag

class FlagUpdate(UpdateView):
    model = Flag
    fields = ['name', 'color']

class FlagDelete(DeleteView):
    model = Flag
    success_url = '/flags/'

