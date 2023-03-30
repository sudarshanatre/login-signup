from django.shortcuts import render , HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def Homepage(request):
    return render (request ,'home.html')

def Signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse('Your password dont match')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
        # return HttpResponse("Your user have been created successfully")
        return redirect('login')
        # print(uname,email,pass1,pass2)

    return render (request,'signup.html')

def Loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')

        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Both username password incorrect")

        # print(username,pass1)
    return render(request ,'login.html')

def Logoutpage(request):
    logout=(request)
    return redirect('login')







