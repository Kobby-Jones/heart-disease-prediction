from django import forms
from .models import HeartDiseasePrediction
from crispy_forms.layout import Layout, Submit, Row, Column
from crispy_forms.helper import FormHelper

class HeartDiseasePredictionForm(forms.ModelForm):
    class Meta:
        model = HeartDiseasePrediction
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HeartDiseasePredictionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('Age', css_class='form-group col-lg-6'),
                Column('Sex', css_class='form-group col-lg-6'),
            ),
            Row(
                Column('Chest pain type', css_class='form-group col-md-6'),
                Column('Trestbps', css_class='form-group col-md-6'),
            ),
            Row(
                Column('Cholestrol level', css_class='form-group col-md-6'),
                Column('Fbs', css_class='form-group col-md-6'),
            ),
            Row(
                Column('Restecg', css_class='form-group col-md-6'),
                Column('Thalac', css_class='form-group col-md-6'),
            ),
            Row(
                Column('Exang', css_class='form-group col-md-6'),
                Column('Oldpeak', css_class='form-group col-md-6'),
            ),
            Row(
                Column('Slope', css_class='form-control col-md-4'),
                Column('Ca', css_class='form-group col-md-4'),
                Column('Thal', css_class='form-group col-md-4'),
            ),
            Submit('submit', 'Predict', css_class='btn btn-primary')
        )