from django.shortcuts import render,redirect
from django.contrib.auth import login as _login, authenticate, logout as _logout
from django.db import IntegrityError
from django.contrib.auth.models import User
from .forms import VacationForm
from django.contrib.auth.decorators import login_required
from .models import Vacation



# if user is not logedin will be redirect to login page. 
# if user is loged in he can add and manage his vacancies
# Create your views here.
@login_required(login_url='/login')
def home(request):
    if request.method == 'GET':
        return render(request,'home.html')
    else:
        form = VacationForm(request.POST)
        newVacation = form.save(commit = False)
        newVacation.employee = request.user
        newVacation.save()
        return redirect('home')


# if user is loged in he will be redirect to home page where he can add or manage his vacancies
# else he will redirect to login page, after loging in he can enter the home page where he can manage his vacancies
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'GET':
            return render(request, 'login/login.html')
        else:
            user = authenticate(
                request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'login/login.html', {'error': 'Username and password did not match'})
            else:
                _login(request, user)
                return redirect('home')


# if the user is register, so he is already loged in and the he will be redirect to home page where he can manage his vacancies
# else we'll get him to register page using 'GET' method and he will apply his signup using the post method
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'GET':
            return render(request, 'register/register.html')
        else:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.save()
                _login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'register/register.html', {'error': 'That username has already been taken. Please choose a new username'})

# if the user is already loggedin he can logout and will be redirect to the login page 
# i have redirect him to home page which will redirect him to the login page because if the user isn't logged in he can't enter the home page  
@login_required
def logout(request):
    if request.method == 'POST':
        _logout(request)
        return redirect('home')
