from django import forms
from .models import HeartDiseasePrediction

class HeartDiseasePredictionForm(forms.ModelForm):
    class Meta:
        model = HeartDiseasePrediction
        exclude = ['prediction_results']

   
    