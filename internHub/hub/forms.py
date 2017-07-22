from django import forms

from .models import Documents, Job


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ('resume', 'cover_letter' )

        
class CreateJobForm(forms.ModelForm): 
    class Meta:
        model = Job
        fields = ('title', 'description', 'skill', 'deadline')
        
