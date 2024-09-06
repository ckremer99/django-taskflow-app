from django.contrib import admin
from .models import Todo, Flag, Subtask

# Register your models here.
admin.site.register(Todo)
admin.site.register(Flag)
admin.site.register(Subtask)