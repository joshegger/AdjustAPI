"""
from django import forms
from .models import Metrics

class MetricsForm(forms.ModelForm):
    class Meta:
        model = "Metrics"
        fields = ('dataset.csv',) """