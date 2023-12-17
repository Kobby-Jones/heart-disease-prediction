from django.shortcuts import render
from .forms import DiabetesForm
from .models import DiabetesPrediction
import joblib
import os
import sklearn
# Load the trained model and the scaler
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ml_models', 'diabetes.pkl')
scaler_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ml_models', 'diabetes_scaler.pkl')
trained_model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Create your views here.
def diabetes_input(request):
    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            pregnancies = form.cleaned_data['pregnancies']
            glucose_Level = form.cleaned_data['glucose_Level']
            blood_Pressure = form.cleaned_data['blood_Pressure']
            skin_Tickness = form.cleaned_data['skin_Tickness']
            insulin = form.cleaned_data['insulin']
            body_Mass_Index = form.cleaned_data['body_Mass_Index']
            diabetes_Pedigree_Function = form.cleaned_data['diabetes_Pedigree_Function']
            age = form.cleaned_data['age'] 

            feature_list = [pregnancies, glucose_Level, blood_Pressure, skin_Tickness,insulin, body_Mass_Index, diabetes_Pedigree_Function, age]
            float_values = [[float(value) for value in feature_list]]
            transformed_data =  scaler.transform(float_values)
            prediction = trained_model.predict(transformed_data)
            DiabetesPrediction.objects.create(pregnancies= pregnancies, glucose_Level=glucose_Level, blood_Pressure = blood_Pressure, skin_Tickness= skin_Tickness, insulin = insulin, body_Mass_Index=body_Mass_Index, diabetes_Pedigree_Function = diabetes_Pedigree_Function, age=age, outcome = prediction[0])

            diabetes_status = {
                "Status": prediction[0]
            }
            return render(request, 'diabetes\outcome.html', diabetes_status)
    else:
        form = DiabetesForm()
    return render(request, 'diabetes\input-data.html', {"form": form})

def diabetes_outcome(request):
    outcome = DiabetesPrediction.objects.last().outcome

    context = {
        "Status": outcome
    }
    return render(request, 'diabetes/outcome.html', context)