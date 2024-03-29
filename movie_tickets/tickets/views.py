from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
@login_required(login_url='login')
def home(request):
    m = movies.objects.all()
    return render(request,'home.html',{'m':m})

def theatreedit(request):
    if request.method=='POST':
        name1=request.POST['Name']
        locations= request.POST['Location']
        the = theatre.objects.create(name=name1,location=locations)
        the.save()
        return redirect('theatrelist')
    return render(request,'theatre.html')
def theatrelist(request):
    t = theatre1.objects.all()
    return render(request,'theatre1.html',{'t':t})
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
        subject="{a} movie ticket".format(a=show.movies.name)
        message="Hi {nam} Here is your ticket infromation\n\nMovie Name:{movie}\nTheatre:{theatre}\nTheatre Location:{theatrelocation}\nNumber of Seats:{seatno}\n\nPrice of one seat:{price}\n\nTotal:{price1}".format(nam=name,movie=show.movies.name,theatre=show.screen.theatre.name,theatrelocation=show.screen.theatre.location,seatno=no_of_seats,price=show.price,price1=(no_of_seats*show.price))
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[request.user.email,]
        send_mail(subject,message,email_from,recipient_list)
        show.save()
        ticket.save()
        return redirect('booked')
    print(show.movies.name)
    return render(request,'book.html',{'show':show})
def cancel(request,id):
    ticket=ticket1.objects.get(id=id)
    show= shows.objects.get(id=ticket.shows.id)
    if request.method == "POST":
        subject="{a} ticket Cancellation".format(a=ticket.shows.movies.name)
        message="Hi {nam} your ticket is Cancelled\n\nMovie Name:{movie}\nTheatre:{theatre}\nTheatre Location:{theatrelocation}\nNumber of Seats:{seatno}\n\nPrice of one seat:{price1}\n\n Total :{price}".format(nam=ticket.name_of_customer,movie=ticket.shows.movies.name,theatre=ticket.shows.screen.theatre.name,theatrelocation=ticket.shows.screen.theatre.location,seatno=ticket.no_of_seats,price=(ticket.no_of_seats*ticket.shows.price),price1=ticket.shows.price)
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[request.user.email,]
        show.no_of_free_seats += ticket.no_of_seats
        show.save()
        send_mail(subject,message,email_from,recipient_list)
        print(ticket.id)
        ticket.delete()
        return redirect('cancelled')
    return render(request,"cancel.html",{'ticket':ticket})
def cancel1(request):
    return render(request,"cancel1.html")   
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
           return HttpResponse("Username Already Exist, Please try a new one")
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exist,Please try with a new email")
            
        if not pass1.isalnum():
            return HttpResponse("Password must be Alpha-Numeric!!")
            
        if len(username)>20:
            return HttpResponse("Username must be under 20 charcters!!")
    
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
            return redirect('home')
        else:
            return HttpResponse("Bad Credentials")
            
    return render(request,'login.html')
def booked(request):
    return render(request,'booked.html')
def logoutP(request):
    logout(request)
    return redirect('login')



