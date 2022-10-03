from django import forms
from django.forms import ModelForm
from .models import Grant

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model=Grant
        fields='__all__'


