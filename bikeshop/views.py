# bikeshopapp/views.py

from django.shortcuts import render, get_object_or_404
from .models import Customers,Brands, Categories, Login, Staffs, Stores, Products, Stocks, Orders, OrderItems


def login(request):
    logins = Login.objects.all()
    return render(request, 'login.html', {'login': logins})

def dashboard(request):
    return render(request, 'dashboard.html')

def customers(request):
    custs = Customers.objects.all()
    return render(request, 'customers.html', {'customers': custs})

def brands(request):
    all_brands = Brands.objects.all()
    return render(request, 'brands.html', {'brands': all_brands})

def categories(request):
    all_categories = Categories.objects.all()
    return render(request, 'categories.html', {'categories': all_categories})

def staffs(request):
    all_staffs = Staffs.objects.all()
    return render(request, 'staffs.html', {'staffs': all_staffs})

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

def order_items(request):
    all_order_items = OrderItems.objects.all()
    return render(request, 'order_items.html', {'order_items': all_order_items})


# Add other views for CRUD operations.
