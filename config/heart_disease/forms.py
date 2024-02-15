from django import forms
from .models import HeartDiseasePrediction
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class HeartDiseasePredictionForm(forms.ModelForm):
    class Meta:
        model = HeartDiseasePrediction
        exclude = ['prediction_results']

   
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User