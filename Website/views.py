from django.shortcuts import render , redirect
from .models import Event
from .forms import BookingForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    dict_eve = {
        'eve':Event.objects.all()
    }
    return render(request,"index.html",dict_eve)

@login_required
def booking(request):

    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking successfully made!')
            return redirect("index")

    form = BookingForm()
    dict_form = {
        'form':form
    }
    return render(request,"booking.html",dict_form)

def register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('register')
            else:
                user_reg = User.objects.create_user(username=username,email=email,password=password)
                user_reg.save()
                messages.info(request,"Successfully created")
                return redirect("/")
        else:
            messages.info(request,"Password does not match")
            return redirect("register")
    return render(request,"register.html")


# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             messages.info(request, "Login Successful")
#             return redirect('/')
#         else:
#             messages.info(request, "Invalid username or password")
#             return redirect("login")  
#     return render(request, 'login.html')

def login_2(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, "Login Successful")
            return redirect('index')
        else:
            messages.info(request, "Invalid username or password")
            return redirect("login")  
    return render(request, 'login_2.html')

def logout(request):
    auth_logout(request)
    return redirect('index')