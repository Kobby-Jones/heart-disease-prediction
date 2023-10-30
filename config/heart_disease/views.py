from django.shortcuts import render
from .models import HeartDiseasePrediction
from .forms import HeartDiseasePredictionForm

# Create your views here.

def user_inputs(request):
    if request.method == 'POST':
        form = HeartDiseasePredictionForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
        # Will process the form data here
        
    else:
        form = HeartDiseasePredictionForm()
    return render(request, 'input_data.html', {'form': form})