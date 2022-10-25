from django.shortcuts import render, redirect
from .forms import signUpForm, logInForm
def home(request):
    return render(request, 'home.html')

def feed(request):
    return render(request, 'feed.html')

def log_in(request):
    form = logInForm()
    return render(request, 'log_in.html', {'form':form})

def sign_up(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = signUpForm()
    return render(request, 'sign_up.html',{'form':form})
