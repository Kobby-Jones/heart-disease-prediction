from django.shortcuts import render
from .forms import DiabetesForm

# Create your views here.
def diabetes_home(request):
    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            return render(request, 'diabetes/input-data.html')
    else:
        form = DiabetesForm()
    return render(request, 'diabetes\input-data.html', {"form": form})