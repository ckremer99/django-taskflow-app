from django.contrib import admin
from .models import Todo, Flag

# Register your models here.
admin.site.register(Todo)
admin.site.register(Flag)