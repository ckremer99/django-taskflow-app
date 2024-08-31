from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('todos/', views.todo_index, name='todo-index'),
    path('todos/<int:todo_id>/', views.todo_detail, name='todo-detail'),
    path('accounts/signup/', views.signup, name='signup'),
]