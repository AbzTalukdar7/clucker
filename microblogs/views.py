from django.shortcuts import render
from .forms import signUpForm

def home(request):
    return render(request, 'home.html')

def sign_up(request):
    form = signUpForm()
    return render(request, 'sign_up.html',{'form':form})
