from django import forms
from .models import HeartDiseasePrediction
from crispy_forms.layout import Layout, Submit, Row, Column, Div, Field
from crispy_forms.helper import FormHelper

class HeartDiseasePredictionForm(forms.ModelForm):
    class Meta:
        model = HeartDiseasePrediction
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HeartDiseasePredictionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-3'
        self.helper.field_class = 'col-4'
        self.helper.layout = Layout(
            Div(
               Div(Field('Age'), css_class='row'),
                Div(Field('Sex'), css_class='row'),
                Div(Field('Chest pain type'), css_class='row'),
                Div(Field('Trestbps'), css_class='row'),
                Div(Field('Cholestrol level'), css_class='row'),
                Div(Field('Fbs'), css_class='row'),
                Div(Field('Restecg'), css_class='row'),
                Div(Field('Thalac'), css_class='row'),
                Div(Field('Exang'), css_class='row'),
                Div(Field('Oldpeak'), css_class='row'),
                Div(Field('Slope'), css_class='row'),
                Div(Field('Ca'), css_class='row'),
                Div(Field('Thal'), css_class='row'),
            )
            )
    