from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Postjob 
from math import ceil
# Create your views here.

Postjobs=Postjob.objects.all()
n=len(Postjobs)
nSlides=n//4 + ceil((n/4)-(n//4))
param={'no_of_slides':nSlides, 'range':range(nSlides),'first':range(0,4),'sec':range(4,n),'Postjob':Postjobs}
def index(request):
    return render(request, 'home.html', param)

    
def contact(request):
    return render(request, 'about.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def jobforyou(request):
    return render(request, 'home.html')
def cvpackage(request):
    return render(request, 'home.html')
def jobpackage(request):
    return render(request, 'home.html')

def user_login(request):
    context={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username ,password=password)
        if user:
            login(request ,user)
            return render(request, 'sucess.html',context)
        else:
            context['error']="valid data"
            return render(request,"login.html",context)
    else:
        return render(request,"login.html",context)

def sucess(request):
        context={}
        user=request.user
        Postjobs=Postjob.objects.all()
        n=len(Postjobs)
        nSlides=n//4 + ceil((n/4)-(n//4))
        context={'user':user,'no_of_slides':nSlides, 'range':range(nSlides),'first':range(0,4),'sec':range(4,n),'Postjob':Postjobs}
        return render(request, 'sucess.html', context )
   

def user_logout(request):
    if request.method=="POST":
        logout(request)
        return render(request, 'home.html')



def register(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                massages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                massages.info(request,'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                first_name=first_name, last_name=last_name)
                user.save();
                print('User Created')
        else:
            print('password not match')
            return redirect('register')
        return redirect('index')
    else: 
        return render(request, "register.html")
    