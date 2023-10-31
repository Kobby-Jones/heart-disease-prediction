from django import forms
from .models import HeartDiseasePrediction
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field
from crispy_forms.helper import FormHelper

class HeartDiseasePredictionForm(forms.ModelForm):
    class Meta:
        model = HeartDiseasePrediction
        exclude = ['prediction_results']

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Column('Age', css_class='form-group col-lg-4'),
            Column('Sex', css_class='form-group col-lg-4'),
            Column('Chest pain type', css_class='form-group col-lg-4'),
        ),
        Row(
            Column('Trestbps', css_class='form-group col-lg-4'),
            Column('Cholestrol level', css_class='form-group col-lg-4'),
            Column('Fbs', css_class='form-group col-lg-4'),
        ),
        Row(
            Column('Restecg', css_class='form-group col-lg-4'),
            Column('Thalac', css_class='form-group col-lg-4'),
            Column('Exang', css_class='form-group col-lg-4'),
        ),
        Row(
            Column('Oldpeak', css_class='form-group col-lg-3'),
            Column('Slope', css_class='form-group col-lg-3'),
            Column('Ca', css_class='form-group col-lg-3'),
            Column('Thal', css_class='form-group col-lg-3'),
        ),

    )
    