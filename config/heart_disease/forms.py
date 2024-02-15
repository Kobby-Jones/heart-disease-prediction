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
    def __init__(self, *args, **kwargs):
         
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['username'].label = False
        self.fields['username'].widget.attrs.update({'placeholder':'Username'})
        self.fields['password1'].help_text = ''
        self.fields['password1'].help_text = ''


class LoginForm(AuthenticationForm):
    class Meta:
        model = User