from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from web_app.models import fleet_data
from django.db import connection

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    
    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, ('Username already exists'))
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, ('Email already exists'))
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name,password=password1,email=email,first_name=f_name,last_name=l_name)
                user.save();
                return redirect('login')
        else:
            messages.info(request, ('Password not matching'))
            return redirect('register')
    else:
        return render(request,"register.html")

    
def login(request):
    
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=user_name,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
        

    else:
        return render(request,'login.html')

def management(request):
    cursor = connection.cursor()
    userid = request.user.id
    cursor.execute("select * from fleet_data join fleet_location on fleet_data.name_plate = fleet_location.name_plate where fleet_data.c_ID = "+str(userid))
    fleets = cursor.fetchall()
    return render(request,'management.html', {'fleets': fleets})