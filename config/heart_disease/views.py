from django.shortcuts import render, redirect
from .models import HeartDiseasePrediction
from .forms import HeartDiseasePredictionForm
import joblib
import os
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression


# Create your views here.
# Load the trained model 
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ml_models', 'trained_model1.pkl')
scaler_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ml_models', 'scaler.pkl')
trained_model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

def home(request):
    return render(request, 'heart_disease/index.html')

def user_inputs(request):
    if request.method == 'POST':
        form = HeartDiseasePredictionForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            chest_pain_type = form.cleaned_data['chest_pain_type']
            trestbps = form.cleaned_data['trestbps']
            cholestrol_level = form.cleaned_data['cholestrol_level']
            fbs = form.cleaned_data['fbs']
            restecg = form.cleaned_data['restecg']
            thalac = form.cleaned_data['thalac']
            exang = form.cleaned_data['exang']
            oldpeak = form.cleaned_data['oldpeak']
            slope = form.cleaned_data['slope']
            ca = form.cleaned_data['ca']
            thal = form.cleaned_data['thal']

            feature_list = [age, sex, chest_pain_type, trestbps, cholestrol_level, fbs, restecg, thalac, exang, oldpeak, slope, ca, thal]
            float_values = [[float(value) for value in feature_list]]
            transfomed_data = scaler.transform(float_values)
            print(transfomed_data.shape)
            prediction = trained_model.predict(transfomed_data)
            HeartDiseasePrediction.objects.create(age=age, sex = sex, chest_pain_type = chest_pain_type, trestbps = trestbps, cholestrol_level = cholestrol_level, fbs = fbs, restecg = restecg, thalac = thalac, exang = exang, oldpeak = oldpeak, slope = slope, ca = ca, thal = thal, prediction_results = prediction[0])

            disease_status = {
                "Results": prediction[0]
            }
            return render(request, 'heart_disease/results.html', disease_status)
        
    else:
        form = HeartDiseasePredictionForm()
    return render(request, 'heart_disease/input_data.html', {'form': form})

def show_results(request):
    prediction_results = HeartDiseasePrediction.objects.last().prediction_results
    context = {
        "Results": prediction_results
    }
    return render(request, 'heart_disease/results.html', context)