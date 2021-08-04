from django.shortcuts import render
from django.shortcuts import render,redirect,reverse,HttpResponseRedirect
from .models import *
from . import forms
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime
from .forms import ContactusForm, OrdernowForm





def food(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def receipe(request):
    return render(request,'receipe.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message = request.POST.get('message')
        obj1=contact(name,phone,email,message)
        obj1.save()
    return render(request,'contactus.html')

    #     print(request.POST)
    #     contactform = ContactusForm(request.POST)
    #     contactform.save()
    # context ={'contactform':contactform}
    # return render(request,'contactus.html')

#     def contact(request):
#     if request.method =="POST":
# name=request.POST.get('name')
# phone=request.POST.get('phone')
# email=request.POST.get('email')
# desc=request.POST.get('desc')
# obj1=Contact(name,phone,email,desc)
# obj1.save()

def order_home(request):
    form = OrdernowForm()
    if request.method == "POST":
        print(request.POST)
        form = OrdernowForm(request.POST)
    context ={'form':form}
    return render(request,'order.html',context)


def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            user.save()
            customer=customerForm.save
            customer.save()
        
            
       

    return render(request,'customersignup.html',context=mydict)
#-----------for checking user iscustomer
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()


@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_home_view(request):
    # bike = models.bike.objects.filter(customer_id = request.user.id)
    # return render(request, 'customerdash.html', {'bike': bike})
    return render(request, 'index.html')


def contact_home(request):
    form = forms.ContactusForm()
    form.save()


# def order_home(request):
#     form = forms.OrdernowForm()
#     mydict= {'form':form}
#     if request.method=="POST":
#         form = OrdernowForm(request.POST,request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.save()
        
#         return HttpResponseRedirect('ordernow')
#     return render(request,'order.html',context=mydict)



def order_home(request):
    form = OrdernowForm()

        
    if request.method == "POST":
        print(request.POST)
        form = OrdernowForm(request.POST)
        
    context ={'form':form}
    return render(request,'order.html',context)

# def order_home(request):
#     form = forms.OrdernowForm()
#     mydict = {'form':form}
#     if request.method == "POST":
#         form = forms.OrdernowForm(request.POST)
   
       
            

#     return render(request,'order.html',context=mydict)

    




    #     userForm=forms.CustomerUserForm()
    # customerForm=forms.CustomerForm()
    # mydict={'userForm':userForm,'customerForm':customerForm}
    # if request.method=='POST':
    #     userForm=forms.CustomerUserForm(request.POST)
    #     customerForm=forms.CustomerForm(request.POST,request.FILES)
    #     if userForm.is_valid() and customerForm.is_valid():
    #         user=userForm.save()
    #         user.save()
    #         customer=customerForm.save
    #         customer.save()
        


def chatroom(request):
    return render(request,"chatroom.html")

     


