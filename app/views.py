from django.shortcuts import render,HttpResponseRedirect
from .forms import signupform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def sign_up(request):
    if request.method =="POST":
        fm = signupform(request.POST)
        if fm.is_valid():
            messages.success(request,'account created successfully')
            fm.save()
    else:
        fm=signupform()
    return render(request,'app/signup.html',{'form':fm})

# login view function

def user_login(request):
    if not request.user.is_authenticated:  #The code request.user.is_authenticated is a Django template variable used to check whether a user is authenticated (logged in) or not. It's commonly used in Django templates to determine whether a user has an active session and can access certain parts of the website.
        if request.method =="POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    #In Django, the code snippet if user is not None is used to check whether a variable named user contains a value or is empty (None). This is a common pattern in programming to ensure that you are working with valid data before proceeding with further operations.
                    login(request, user)
                    #In short, login(request, user) is like granting a user access to your website's protected areas by creating a session for them. This allows them to navigate around as a recognized party guest.
                    messages.success(request,'logged in successfully')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'app/userlogin.html', {'form':fm})                
    else:
        return HttpResponseRedirect('/profile/')    
    
# profile views
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'app/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

# logout

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')






