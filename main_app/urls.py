from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('todos/', views.todo_index, name='todo-index'),
    path('todos/<int:todo_id>/', views.todo_detail, name='todo-detail'),
    path('todos/create/', views.TodoCreate.as_view(), name='todo-create'),
    path('todos/<int:pk>/update', views.TodoUpdate.as_view(), name='todo-update'),
    path('todos/<int:pk>/delete', views.TodoDelete.as_view(), name='todo-delete'),
    path('accounts/signup/', views.signup, name='signup'),
]