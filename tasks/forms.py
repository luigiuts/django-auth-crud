
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','descripcion','important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Escribe un titulo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Escribe una descripcion'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'})
        }