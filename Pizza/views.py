from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import PizzaModel

# Create your views here.

def adminloginview(request):
    name = 'omesh kumar'
    context = {'name': name}
    return render(request,"pizza/adminlogin.html", context)

def authenticationadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username, password=password)

    # user exist
    if user is not None and user.username =="admin":
        login(request, user)
        return redirect('adminhomepage')
    
    # user doesn't exist
    if user is None:
        messages.add_message(request, messages.ERROR,"invalid credentials")
        return redirect('adminloginpage')
        # error = "Credentials are invalid"
        # context= {"error": error}
        # return render(request, "pizza/adminlogin.html", context)
       

def adminhomepageview(request):
    context ={'pizzas' : PizzaModel.objects.all()}
    return render(request, "pizza/adminhomepage.html", context)

def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')

def addpizza(request):
    name = request.POST['pizza']
    price = request.POST['price']
    PizzaModel(name = name, price = price).save()
    return redirect('adminhomepage')

def deletepizza(request, pizzapk):
    PizzaModel.objects.filter(id = pizzapk).delete()
    return redirect('adminhomepage')

def homepageview(request):
    return render(request, "pizza/homepage.html")

def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    phoneno = request.POST['']