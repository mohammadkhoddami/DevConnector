from django.shortcuts import render , redirect
from .models import User, Userprofile
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def addeducation(request):
    return render(request, 'accounts/add-education.html', {})

def addexperience(request):

    return render(request, 'accounts/add-experience.html', {})

def createprofile(request):
    return render(request, 'accounts/create-profile.html', {})

def dashboard(request):
    return render(request, 'accounts/dashboard.html', {})


def login(request):
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(request, username=u, password=p)
        if user is not None:
            django_login(request, user)
            return redirect(reverse('profile', args=[user.pk]))
        return render(request, 'accounts/login.html', {})
    else :
        return render(request, 'accounts/login.html', {})

@login_required
def profile(request, pk):
    user_profile = Userprofile.objects.get(pk = pk)
    return render(request, 'accounts/profile.html', {"user_profile": user_profile})

def profiles(request):
    return render(request, 'accounts/profiles.html', {})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #print(form)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            #print(user)
            #print(username, password)
            user = authenticate(username=username, password=password)
            django_login(request, user)
            return redirect('/index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form' : form})

def user_logout(request):
    logout(request)
    return redirect('/index')



