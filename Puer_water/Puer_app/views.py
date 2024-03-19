from django.shortcuts import render
from django .http import HttpResponse
from Puer_app import views

# Create your views here.

def home(request):
    return render(request, 'Puer_app/index.html')



def form(request):
    diction ={}
    return render(request, 'Puer_app/form.html', context=diction)