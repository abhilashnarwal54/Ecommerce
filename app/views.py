from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.db.models import Count
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from .models import Customers

#home section
def home(request):
    return render(request, 'home.html')
#about section
def about(request):
    return render(request, 'about.html')
#contacts section
def contact(request):
    return render(request, 'contact.html')
#product category section
class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'category.html',locals())
#based on the title it will show product
#when click the some title it will show that particular product
class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'category.html',locals())
#for particular product details
class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'productdetails.html',locals())

#registration section

def Registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 =request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name alredy registerd')
                return redirect(request,'login.html')
            elif User.objects.filter(password=password).exists():
                messages.info(request,'password is alredy registerd')
                return render('login.html')
            else:   
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request,'user created')
                return render(request,'login.html')

        else:
            messages.info(request,'password is not matching')
            return render('customersregistration.html')
        return rednder(request,'customersregistration.html')
        
    else:
        return render(request,'customersregistration.html')

#login page
def Login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request,'Logged in Sucessfully')
            return render(request,'login.html')
        else:
            messages.info(request,'invalid credentials')
            return render('login.html')
    else:
        return render(request,'login.html')    
        

#logout
def Logout(request):
    auth.logout(request)
    return redirect('/')

#profile section
class ProfileView(View):
    def get(self,request):
        form= CustomerProfileForm()
        return render(request,'profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city'] 
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user,name=name, locality=locality, city=city, mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request,"Profile saved Sucessfully")
        else:
            messages.warning(request,'Invalid Data')

        return render(request,'profile.html',locals())

#address section
def address(request):
    add = Customers.objects.filter(user=request.user)
    return render(request,'address.html',locals())

#update address
class UpdateAdress(View):
    def get(self,request,pk):
        add = Customers.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'updateaddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city'] 
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,'Profile Updated Successfully')
        else:
            messages.warning(request,"Invalid Input data")
        return redirect('address')


# Create your views here.
