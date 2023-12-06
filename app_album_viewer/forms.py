from django import forms
from .models import Song

class AddSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'runtime']