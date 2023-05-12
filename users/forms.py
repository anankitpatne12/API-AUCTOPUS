from django import forms
from .models import StudData

class UserForm(forms.ModelForm):
    class Meta:
        model = StudData
        fields = '__all__'