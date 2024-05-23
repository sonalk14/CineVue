from django.shortcuts import render,redirect,HttpResponse
from.models import Movie,Wishlist,Subscriptions,Suborder
from django.views.generic .detail import DetailView
from django.db.models import Q
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import razorpay
import random
from django.core.mail import send_mail

# Create your views here.
def base(req):
    m = Movie.objects.all()
    print(m)
    context ={'movie':m}
    return render(req,'home.html',context)

class Specific(DetailView):
    model = Movie
    template_name = "play.html"

def moviesDisplay(req):
    m= Movie.objects.all()
    print(m)
    context={'movie':m}
    return render(req,'movies.html',context)

def search(req):
    query =req.POST.get('q')
    results= Movie.objects.filter(Q(name__icontains = query)|Q(desc__icontains = query)|Q(year__icontains = query)|Q(category__icontains=query))
    context = {'movie':results}
    return render(req,'home.html',context)


def searchM(req):
    query =req.POST.get('q')
    results= Movie.objects.filter(Q(name__icontains = query)|Q(desc__icontains = query)|Q(year__icontains = query)|Q(category__icontains=query))
    context = {'movie':results}
    return render(req,'movies.html',context)

def wish(req):
    return render(req,"wishlist.html")
 
def addWishlist(req,movie_id):
    try:
        movies = Movie.objects.get(m_id = movie_id)
        user = req.user if req.user.is_authenticated else None
        print(user)
        if user:
            w_item,created = Wishlist.objects.get_or_create(movie = movies,user=user)
        print(w_item,created)
        if not created:
            w_item.quantity += 1
        else:
            w_item.quantity = 1
        
            
        #prod = Wishlist.objects.all()
        #print(prod[0])
        w_item.save()
        return redirect("/viewWishlist")
    except:
        return redirect("login")


def viewWishlist(req):
    try:
        prod = Wishlist.objects.filter(user = req.user)
        print(prod)
        context ={'movies':prod}
        return render(req,'wishlist.html',context)
    except:
        return redirect("login")


def deleteWishlist(req,item_id):
    movies = Wishlist.objects.filter(movie_id = item_id)
    movies.delete()
    return redirect("/viewWishlist")

def register(req):
    #form = UserCreationForm() default form
    form = CreateUserForm()
    if req.method == "POST":
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
            print("User created successfully")
            return redirect("/login")
        else:
            messages.error(req,"Your username or password format is invalid")
    context = {'form':form}
    return render(req,"registration.html",context)

def login_user(req):
    if req.method == "GET":
        return render(req,"login.html")
    else:
        username = req.POST["uname"]
        passw = req.POST["upass"]
        #print(username,password)
        user = authenticate(req,username=username,password=passw)
        if user is not None:
            login(req,user)
            req.session['uname']=username
            messages.success(req,"Logged in successfully")
            return redirect("/")
        else:
            messages.error(req,"there was an error.Try again")
            return redirect("/login")
         

def logout_user(req):
    try:
        logout(req)
        del req.session['uname'];
        messages.success(req,"you have logged out successfully")
        return redirect("/")
    except:
        logout(req)
        messages.success(req,"you have logged out successfully")
        return redirect("/")
    
def sub(req):
    sub = Subscriptions.objects.all()
    context={'movie':sub}
    return render(req,"subscription.html",context)

def sendMail(req):

    usermail = req.user.email
    print(usermail)
    print(req.user) 
    orders = Suborder.objects.filter(user = req.user,is_completed = True)
    print(orders)
    total_price = 0
    for x in orders:
        total_price = x.subo.price
        oid = x.order_id
        name = x.subo.name

    
    send_mail(
    "you have subscribed successfully",
    "you have subscribed successfully",
    "sonalkeluskar14@gmail.com",
    [usermail],
    fail_silently=False,
)
    return redirect("/")

def buy(req,prod_id):
    
       
        oid = random.randrange(1000,9999)
        oid = str(oid)

        prod = Subscriptions.objects.get(s_id = prod_id)
        print(prod.price)
        orders = Suborder.objects.create(order_id = oid,subo =prod,user=req.user)
        client =razorpay.Client(auth=("rzp_test_DkcjEIBCdzwWxA","t47nLvoQow0AHEOr0d5aNLze"))
        total_price = prod.price*100
        data = {'amount':total_price,"currency":'INR',"receipt":oid}
        payment = client.order.create(data=data)
        context = {'data':payment}
        orders = Suborder.objects.filter(user=req.user,is_completed=False)
        return render(req,'payment.html',context)
   
def horror(req):
   queryset=Movie.objects.filter(category__iexact="horror")
   context = {'movie':queryset}
   return render(req,"movies.html",context)

def comedy(req):
   queryset=Movie.objects.filter(category__iexact="comedy")
   context = {'movie':queryset}
   return render(req,"movies.html",context)
def adventure(req):
   queryset=Movie.objects.filter(category__iexact="adventure")
   context = {'movie':queryset}
   return render(req,"movies.html",context)