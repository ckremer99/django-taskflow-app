from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Todo, Flag, Subtask
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import TodoForm, CompletedForm, SubtaskForm, SubtaskCompletedForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

@login_required
def todo_index(request):
    flags = Flag.objects.filter(user=request.user)
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/index.html/', 
        { "todos": todos, "flags": flags })

@login_required
def todo_detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    flags_todo_doesnt_have = Flag.objects.exclude(id__in = todo.flags.all().values_list('id'))
    flags = todo.flags.all()
    completed_form = CompletedForm(instance=todo)
    subtask_form = SubtaskForm()
    subtasks = Subtask.objects.filter(todo=todo)
    subtask_completed_form = SubtaskCompletedForm()
    
    
    return render(request, 'todos/detail.html', {
         'todo': todo,
         'flags_todo_doesnt_have': flags_todo_doesnt_have,
         'flags': flags,
         'completed_form': completed_form,
         'subtask_form': subtask_form,
         'subtasks': subtasks,
         'subtask_completed_form': subtask_completed_form,
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

@login_required
def associate_flag(request, todo_id, flag_id):
    Todo.objects.get(id=todo_id).flags.add(flag_id)
    return redirect('todo-detail', todo_id=todo_id)

@login_required
def remove_flag(request, todo_id, flag_id):
    Todo.objects.get(id=todo_id).flags.remove(flag_id)
    return redirect('todo-detail', todo_id=todo_id)

@login_required
def update_completed(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo-detail', todo_id=todo_id)

@login_required
def subtask_create(request, todo_id):
    form = SubtaskForm(request.POST)
    if form.is_valid():
        new_subtask = form.save(commit=False)
        new_subtask.todo_id = todo_id
        new_subtask.completed = False
        new_subtask.save()
    return redirect('todo-detail', todo_id=todo_id)
        
@login_required
def subtask_checkbox(request, todo_id, pk):
    subtask = Subtask.objects.get(id=pk)
    subtask.completed = not subtask.completed
    subtask.save()
    return redirect('todo-detail', todo_id=todo_id)

@login_required
def filter_todos(request):
    flags = Flag.objects.filter(user=request.user)
    if request.method == 'POST': 
        flag = request.POST.get('select-flag', False)
        show_completed = True if request.POST.get('show-completed', False) == 'on' else False
        if flag == 'All':
            if not show_completed:
                todos = Todo.objects.filter(user=request.user, completed=False)
            else:
                todos = Todo.objects.filter(user=request.user)
        else:
            if not show_completed:
                todos = Todo.objects.filter(user=request.user, completed=False, flags__name=flag)
            else: 
                todos = Todo.objects.filter(user=request.user, flags__name=flag)
    return render(request, "todos/index.html", {
        "show_completed": show_completed,
        "todos": todos,
        "flags": flags, 
    })
    


class TodoCreate(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm

class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = '/todos/'

class FlagCreate(LoginRequiredMixin, CreateView): 
    model = Flag
    fields = ['name', 'color'] 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FlagList(LoginRequiredMixin, ListView):
    model = Flag

class FlagDetail(LoginRequiredMixin, DetailView):
    model = Flag

class FlagUpdate(LoginRequiredMixin, UpdateView):
    model = Flag
    fields = ['name', 'color']

class FlagDelete(LoginRequiredMixin, DeleteView):
    model = Flag
    success_url = '/flags/'

