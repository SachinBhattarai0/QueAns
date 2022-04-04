from django.shortcuts import redirect, render
from .models import profiles
from .forms import customUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import profileForm


# Create your views here.
def loginPage(request):
    context={'page':'login'}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('main')
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('login')
        else:
            messages.info(request,'Username Doesnot Exists')
            return redirect('login')
    return render(request,'users/login_register.html',context)


def registerPage(request):
    context={'page':'register','form':customUserCreationForm()}
    if request.method == 'POST':
        newuser = UserCreationForm(request.POST)
        if User.objects.filter(username=request.POST['username']).exists():
            messages.info(request,'Username Already Exists')
            return redirect('register')
        else:
            if newuser.is_valid():
                newuser.save()
                messages.info(request,'User Created Succesfully.Please Login')
                return redirect('login')
            else:
                messages.info(request,'Credentials not valid')
                return redirect('register')

    return render(request,'users/login_register.html',context)


def logoutPage(request):
    logout(request)
    return redirect('main')

def editProfile(request):
    user = profiles.objects.get(name=request.user)
    form = profileForm(instance=user)
    if request.method == 'POST':
        form = profileForm(request.POST,request.FILES,instance=user)
        if form.is_valid:
            form.save()
            return redirect('main')
    context = {'form':form}
    return render(request,'users/edit-profile.html',context)

@login_required(login_url='login')
def profile(request,pk):
    userinfo = User.objects.get(username=pk)
    context={'userinfo':userinfo}
    return render(request,'users/profile.html',context)


