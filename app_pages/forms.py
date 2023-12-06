from django import forms
from .models import EmailForm

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailForm
        fields = ['to', 'title', 'message']