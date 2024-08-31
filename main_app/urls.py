from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.todo_index, name='todo-index'),
    path('todos/<int:todo_id>/', views.todo_detail, name='todo-detail'),
]