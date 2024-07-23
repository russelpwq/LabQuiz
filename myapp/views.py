from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PasswordForm

def home(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            return redirect('welcome', password=password)
    else:
        form = PasswordForm()

    return render(request, 'home.html', {'form': form})

def welcome(request, password):
    return render(request, 'welcome.html', {'password': password})

def logout_view(request):
    return redirect('home')