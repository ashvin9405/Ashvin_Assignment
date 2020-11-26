from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . import views
from .models import Employee
# Create your views here.
def contact(request):
    return HttpResponse("My contact: Ashvin Bhutekar \n Mob No. 9405779777")

def overview(request):
    return render(request,'overview.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
        else:
            auth.login(request, user)
            return redirect('/')
    else:

        return render(request,'login.html')
        

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first Name']
        lastname=request.POST['Last Name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=firstname, last_name=lastname)
                user.save();
                print("created user")
                return redirect('login')
        else:
            messages.info(request, "Password not matching!!")
            return redirect('signup')
        return redirect('/')
    else:
        return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def employee(request):  #here members is name of function
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        salary = request.POST['salary']


        e = Employee(name=name, address=address,salary=salary)   # Membership is class/model/table written in models.py name is field in model and function and should be mapped properly
        e.save()
        return redirect('/')
    else:
        emp = Employee.objects.all()       # p contains all the objects(rows) in the Membership table
        return render(request,'employee.html',{"s2":emp})


