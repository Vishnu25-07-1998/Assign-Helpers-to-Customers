from django.shortcuts import render, redirect
from .models import Helper, Customer
import json

# Create your views here.

def home(request):
    return render(request, 'home.html')

def AddHelper(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        skill = request.POST.get('skill')
        age = request.POST.get('age')
        print('age = ', age) 
        print('skill = ', skill)  
        Helpers = Helper.objects.create(name=name, gender=gender, skill=skill, age=age)

        Helpers.save()
        if Helpers:
            return redirect('HelperDetails')
    return render(request,'AddHelper.html')

def AddCustomer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        age = request.POST.get('age') 
        address = request.POST.get('address')
        print('age = ', age) 

        Customers = Customer.objects.create(name=name, gender=gender, address = address, age=age)

        Customers.save()
        if Customers:
            return redirect('CustomerDetails')
    return render(request,'AddCustomer.html')

def AssignHelper(request):
    Customers = Customer.objects.all()
    Helpers = Helper.objects.all()

    if request.method == 'POST':
        Customer_name = request.POST.get('Customer')
        print(Customer_name )
        skill = request.POST.get('skill')
        print(skill)
        Helper_name = request.POST.get('helper')
        print(Helper_name)
        return redirect('assigned_helper', customer_name=Customer_name, helper_name=Helper_name, skill=skill)



    context = {
        'Customers' : Customers,
        'Helpers': Helpers,
    }
    return render(request,'AssignHelper.html', context)

def AssignedHelper(request, customer_name, helper_name, skill):
    context = {
        'customer_name': customer_name,
        'helper_name': helper_name,
        'skill': skill,
    }
    return render(request, 'AssignedHelper.html', context)

def CustomerDetails(request):
    Customers = Customer.objects.all()
    Helpers = Helper.objects.all()
    context = {
        'Customers' : Customers,
        'Helpers': Helpers,
    }
    return render(request, 'customerDetails.html', context)

def HelperDetails(request):
    Customers = Customer.objects.all()
    Helpers = Helper.objects.all()
    context = {
        'Customers' : Customers,
        'Helpers': Helpers,
    }
    return render(request, 'HelperDetails.html', context)
