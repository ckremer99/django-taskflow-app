from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('todos/', views.todo_index, name='todo-index'),
    path('todos/<int:todo_id>/', views.todo_detail, name='todo-detail'),
    path('todos/create/', views.TodoCreate.as_view(), name='todo-create'),
    path('todos/<int:pk>/update/', views.TodoUpdate.as_view(), name='todo-update'),
    path('todos/<int:pk>/delete/', views.TodoDelete.as_view(), name='todo-delete'),
    path('flags/create/', views.FlagCreate.as_view(), name='flag-create'),
    path('todos/<int:todo_id>/associate-flag/<int:flag_id>/', views.associate_flag, name='associate-flag'),
    path('todos/<int:todo_id>/remove-flag/<int:flag_id>/', views.remove_flag, name='remove-flag'),
    path('todos/<int:todo_id>/update-completed/', views.update_completed, name='todo-completed'),
    path('flags/<int:pk>/', views.FlagDetail.as_view(), name='flag-detail'),
    path('flags/', views.FlagList.as_view(), name='flag-index'),
    path('flags/<int:pk>/update/', views.FlagUpdate.as_view(), name='flag-update'),
    path('flags/<int:pk>/delete/', views.FlagDelete.as_view(), name='flag-delete'),
    path('subtasks/<int:todo_id>/add', views.subtask_create, name='subtask-create'),
    path('subtasks/<int:todo_id>/<int:pk>/completed/', views.subtask_checkbox, name='subtask-checkbox'),
    path('accounts/signup/', views.signup, name='signup'),
]