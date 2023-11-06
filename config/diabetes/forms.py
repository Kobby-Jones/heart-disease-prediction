from django import forms
from .models import DiabetesPrediction

class DiabetesForm(forms.ModelForm):
    class Meta:
        model = DiabetesPrediction
        exclude = ['outcome']