from django import forms

from .models import Program


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('name', 'description', 'location', 'codebase', 'last_commit_time', 'last_commit_user', )
