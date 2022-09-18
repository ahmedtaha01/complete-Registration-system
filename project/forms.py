from django import forms
from django.forms import ModelForm
from .models import Project
from datetime import date

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
    
    def clean_project_end_date(self):
        start_date = self.cleaned_data.get('project_start_date')
        end_date = self.cleaned_data.get('project_end_date')
        if (not end_date is None) and  end_date < start_date:
            raise forms.ValidationError('Ending date has to be after starting date.')
        return end_date
