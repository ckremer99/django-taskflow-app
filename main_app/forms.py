from django import forms
from .models import Todo, Subtask

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

class SubtaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['title', 'due']
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

class SubtaskCompletedForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['completed']
    