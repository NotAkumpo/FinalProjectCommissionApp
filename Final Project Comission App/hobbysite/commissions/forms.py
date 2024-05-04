from django import forms
from datetime import datetime

from .models import Commission, Job, JobApplication


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'author', 'status']
        widgets = {
            'author': forms.TextInput(
                attrs={ 'readonly':'readonly' }
            )
        }

    created_at = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}), initial='Current Time')
    updated_at = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}), initial='Current Time')


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'manpowerRequired', 'status']
        

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job']

    def __init__(self, *args, **kwargs):
        available_jobs = kwargs.pop('available_jobs', None)
        no_jobs = kwargs.pop('no_jobs', False)
        super().__init__(*args, **kwargs)
        if available_jobs:
            self.fields['job'].queryset = available_jobs.filter(openManpower__gt=0)
        if no_jobs:
            self.fields['job'].queryset = self.fields['job'].queryset.none()