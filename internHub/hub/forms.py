from django import forms

from .models import Documents

from material import *

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ('resume', 'cover_letter' )

class CreateJobForm(forms.Form):
    title = forms.CharField()
    employer = forms.CharField()

    skill = forms.ChoiceField(choices=((None, 'Skill level'), 
        ('J', 'Junior'),
        ('I', 'Intermediate'),
        ('S', 'Senior'),))
    description = forms.CharField(widget=forms.Textarea)

    layout = Layout('title', 'employer', 'skill', 'description')