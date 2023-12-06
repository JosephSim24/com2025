from django import forms
from .models import Album

class AddSongForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['songs']