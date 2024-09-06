from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Flag(models.Model):
    name = models.CharField(max_length = 100)
    color = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('todo-index')


class Todo(models.Model):
    title = models.CharField(max_length=100)
    due = models.DateField()
    description = models.TextField(max_length=250)
    flags = models.ManyToManyField(Flag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
         return self.title

    def get_absolute_url(self):
            return reverse('todo-detail', kwargs={'todo_id': self.id})

class Subtask(models.Model):
    title = models.CharField(max_length=250)
    due = models.DateField('Date Due')
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title
    





