from django import forms

from .models import Documents


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ('resume', 'cover_letter' )
