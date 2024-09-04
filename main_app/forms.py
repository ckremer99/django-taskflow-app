from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'due', 'description']
        widgets = {
            'due': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

class CompletedForm(forms.ModelForm):
    class Meta: 
        model = Todo
        fields = ['completed']