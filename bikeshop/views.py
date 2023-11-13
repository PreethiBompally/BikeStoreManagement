# bikeshopapp/views.py

from django.shortcuts import render, get_object_or_404
from .models import Customers, Login, Registration, Staff, Stores, Products, Stocks, Orders


def login(request):
    logins = Login.objects.all()
    return render(request, 'login.html', {'login': logins})

def dashboard(request):
    return render(request, 'dashboard.html')

def customers(request):
    custs = Customers.objects.all()
    return render(request, 'customers.html', {'customers': custs})

def staff(request):
    all_staff = Staff.objects.all()
    return render(request, 'staff.html', {'staff': all_staff})

def stores(request):
    all_stores = Stores.objects.all()
    return render(request, 'stores.html', {'stores': all_stores})

def products(request):
    all_products = Products.objects.all()
    return render(request, 'products.html', {'products': all_products})

def stocks(request):
    all_stocks = Stocks.objects.all()
    return render(request, 'stocks.html', {'stocks': all_stocks})

def orders(request):
    all_orders = Orders.objects.all()
    return render(request, 'orders.html', {'orders': all_orders})

def registration(request):
    all_reg = Registration.objects.all()
    return render(request, 'registration.html', {'registration': all_reg})

def aboutus(request):
    return render(request, 'aboutus.html')
def contact(request):
    return render(request, 'contact.html')


# Add other views for CRUD operations.
