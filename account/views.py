from django.shortcuts import render, redirect
from account.forms import RegisterForm
from django.contrib.auth import login, authenticate
# Create your views here.

def signup_view(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, 'registration/signup.html', {'form': form})

def profile_view(request):
    return render(request,'account/profile.html')
