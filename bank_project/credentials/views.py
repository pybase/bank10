from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bank_app:details')
        else:
            messages.info(request, 'invalid login')


    return render(request,'login.html')


def register(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if User.objects.filter(username=username).exists():
            messages.info(request,'username already exist')
            return  redirect('credentials:register')
        else:
         user = User.objects.create_user(username=username, password=password)
         user.save();
         return  redirect('credentials:login')


    return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')