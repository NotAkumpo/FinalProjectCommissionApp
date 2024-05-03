from django import forms
from datetime import datetime

from .models import Commission, JobApplication


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'
        widgets = {
            'author': forms.TextInput(
                attrs={ 'readonly':'readonly' }
            )
        }

    created_at = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}), initial='Current Time')
    updated_at = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}), initial='Current Time')


class JobApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        available_jobs = kwargs.pop('available_jobs', None)
        no_jobs = kwargs.pop('no_jobs', False)
        super().__init__(*args, **kwargs)
        if available_jobs:
            self.fields['job'].queryset = available_jobs
        if no_jobs:
            self.fields['job'].queryset = self.fields['job'].queryset.none()
        
    class Meta:
        model = JobApplication
        fields = ['job']