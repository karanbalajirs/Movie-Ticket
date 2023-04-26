from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
@login_required(login_url='login')
def home(request):
    m = movies.objects.all()
    return render(request,'home.html',{'m':m})
def booking_page(request,id):
    movie=movies.objects.get(movies=id)
    show=shows.objects.filter(movies=id)
    return render(request,'booking.html',context={'movie':movie,'show':show})
    
def book(request,id):
    show=shows.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['Name']
        no_of_seats= request.POST['NoOfSeats']
        no_of_seats=int(no_of_seats)
        age1=request.POST['Age']
        age1=int(age1)
        print(name,no_of_seats,age1,request.user)
        if(int(no_of_seats) > show.no_of_free_seats):
            return HttpResponse("Number of selected seats is not available")
        ticket = ticket1.objects.create(userid=request.user,shows=show,name_of_customer=name,age=age1,no_of_seats=no_of_seats)
        show.no_of_free_seats -= no_of_seats
        show.save()
        ticket.save()
        return redirect('booked')
    print(show.movies.name)
    return render(request,'book.html',{'show':show})
def ticket(request):
    ticket=ticket1.objects.filter(userid=request.user)
    return render(request,"ticket.html",{'ticket':ticket})
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if User.objects.filter(username=username):
            messages.error(request,"Username Already Exist, Please try a new one")
            return redirect('home')
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exist,Please try with a new email")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        if (pass1!=pass2):
            return HttpResponse("Both passwords are not the same!")
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        return redirect('login')
        
        
    return render(request, "signup.html")

def loginP(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.error(request,"Hi {us}".format(us=user.username))
            return redirect('home')
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')
    return render(request,'login.html')
def booked(request):
    return render(request,'booked.html')
def logoutP(request):
    logout(request)
    return redirect('login')



