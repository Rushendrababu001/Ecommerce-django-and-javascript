from django.shortcuts import render,redirect,HttpResponse
from shop.form import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,"shop/index.html", {"products":products})

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully")
        return redirect("/")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name")
                return redirect("/login")
        return render(request,"shop/login.html")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration success you can Login now")
            return redirect('/login')
    return render(request,"shop/register.html", {'form':form})

def collections(request):
    category=Category.objects.filter(status=0)
    return render(request,"shop/collections.html", {"category":category})
  
def collectionsview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)        
        return render(request,"shop/products/index.html", {"products":products, "category":name})
    else:
        messages.warning(request="No Category Found")
        return redirect('collections')
    
def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            product=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html", {"product":product})
        else:
            messages.error(request,"Product not Found")
            return redirect('collections')
    else:
        messages.error(request,"Category Not Found")
        return redirect('collections')