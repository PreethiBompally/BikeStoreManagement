# bikeshopapp/views.py
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Customers, Products, Stocks, Orders
from django.urls import reverse
from staff.models import Staff,Stores
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        staff = authenticate(request, USER_NAME=username, password=password)
        if staff is not None:
            login(request,staff)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login_view.html',{'error': 'Invalid username or password'})
    else:
        return render(request, 'login_view.html')

def logout_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'logout.html')
    else:
        return render(request, 'dashboard.html')
    
def registration(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        image_url = request.POST['image_url']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # Create a new Staff instance and save it to the database
        staff=Staff.objects.create_user(
        USER_NAME=user_name,
        EMAIL=email,
        password=password1,
        FIRST_NAME=first_name,
        LAST_NAME=last_name,
        PHONE=phone if phone != '' else None,
        IMAGE_URL=image_url)
        
        return HttpResponseRedirect(reverse('login_view'))
    else:
        return render(request, 'registration.html')

def dashboard(request):
    user_info = None
    if request.user.is_authenticated:
        user_info = {'user_name': request.user.USER_NAME}
        print(request.user.USER_NAME)
    return render(request, 'dashboard.html', {'user_info': user_info})

def staff(request):
    all_staff = Staff.objects.all()
    return render(request, 'staff.html', {'staff': all_staff})

def edit_staff(request,staff_id):
    staff = get_object_or_404(Staff, STAFF_ID=staff_id)
    
    context = {'staff':staff}
    return render(request, 'staff_details.html', context)

def delete_staff(request, staff_id):
    if request.method == 'GET':
        staff = get_object_or_404(Staff, STAFF_ID=staff_id)
        staff.delete()
        return redirect('staff')

def stores(request):
    all_stores = Stores.objects.all()
    return render(request, 'stores.html', {'stores': all_stores})

def stocks(request):
    all_stocks = Stocks.objects.all()
    
    if request.method == 'POST':
        search_str = request.POST.get('search')
        filter_value = request.POST.get('filter')
        if filter_value != '' and search_str != '':
            if filter_value == 'STORE_NAME':
                store = Stores.objects.filter(STORE_NAME__icontains=search_str).values('STORE_ID')
                if store:
                    all_stocks = all_stocks.filter(STORE_ID=store[0]['STORE_ID'])
            elif filter_value == 'PRODUCT_NAME':
                product = Products.objects.filter(PRODUCT_NAME__icontains=search_str).values('PRODUCT_ID')
                if product:
                    all_stocks = all_stocks.filter(PRODUCT_ID=product[0]['PRODUCT_ID'])

    store_ids = set(stock.STORE_ID for stock in all_stocks)
    product_ids = set(stock.PRODUCT_ID for stock in all_stocks)

    store_names = {store.STORE_ID: store.STORE_NAME for store in Stores.objects.filter(STORE_ID__in=store_ids)}
    product_names = {product.PRODUCT_ID: product.PRODUCT_NAME for product in Products.objects.filter(PRODUCT_ID__in=product_ids)}

    for stock in all_stocks:
        stock.STORE_ID = store_names.get(stock.STORE_ID, '')
        stock.PRODUCT_ID = product_names.get(stock.PRODUCT_ID, '')

    page = request.GET.get('page')
    items_per_page = request.GET.get('items_per_page',10)
    paginator = Paginator(all_stocks, items_per_page)
    try:
        all_stocks = paginator.page(page)
    except PageNotAnInteger:
        all_stocks = paginator.page(1)
    except EmptyPage:
        all_stocks = paginator.page(paginator.num_pages)
    
    return render(request, 'stocks.html', {'stocks': all_stocks})

def orders(request):
    all_orders = Orders.objects.all().order_by('ORDER_ID')
    
    if request.method == 'POST':
        search_str = request.POST.get('search')
        filter_value = request.POST.get('filter')
        if filter_value != '' and search_str != '':
            if filter_value == 'ORDER_ID':
                all_orders = all_orders.filter(ORDER_ID=search_str)
            elif filter_value == 'STORE_NAME':
                store = Stores.objects.filter(STORE_NAME__icontains=search_str).values('STORE_ID')
                if store:
                    all_orders = all_orders.filter(STORE_id__in=store)
            elif filter_value == 'CUSTOMER_NAME':
                customer = Customers.objects.filter(Q(FIRST_NAME__icontains=search_str) | Q(LAST_NAME__icontains=search_str)).values('CUSTOMER_ID')
                if customer:
                    all_orders = all_orders.filter(CUSTOMER_id__in=customer)
            elif filter_value == 'PRODUCT_NAME':
                product = Products.objects.filter(PRODUCT_NAME__icontains=search_str).values('PRODUCT_ID')
                if product:
                    all_orders = all_orders.filter(PRODUCT_id__in=product)
    page = request.GET.get('page')
    items_per_page = request.GET.get('items_per_page',10)
    paginator = Paginator(all_orders, items_per_page)
    try:
        all_orders = paginator.page(page)
    except PageNotAnInteger:
        all_orders = paginator.page(1)
    except EmptyPage:
        all_orders = paginator.page(paginator.num_pages)
        
    return render(request, 'orders.html', {'orders': all_orders})

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    all_products = Products.objects.all()
    context= {'products': all_products}
    if request.method == 'POST':
        search_str = request.POST.get('search')
        filter_value = request.POST.get('filter')
        print("here"+search_str+"here")
        if(filter_value != '' and search_str != ''):
            if(filter_value == 'brand'):
                all_products = Products.objects.filter(BRAND_NAME__icontains=search_str)
            if(filter_value == 'category'):
                all_products = Products.objects.filter(CATEGORY_NAME__icontains=search_str)
            if(filter_value == 'year'):
                all_products = Products.objects.filter(MODEL_YEAR__icontains=search_str)
        context= {'products': all_products}
        return render(request, 'products.html', context)
    else:
        return render(request, 'products.html', context)

def add_product(request):
    print(request.POST['product_id'] if 'product_id' in request.POST else "")
    
    distinct_brands = Products.objects.values_list('BRAND_NAME', flat=True).distinct()
    distinct_categories = Products.objects.values_list('CATEGORY_NAME', flat=True).distinct()

    if request.method == 'POST':
        if 'product_id' in request.POST and request.POST['product_id'] != '':
            product_id = request.POST['product_id']
            product = get_object_or_404(Products, PRODUCT_ID=product_id)
            product.PRODUCT_NAME = request.POST['product_name']
            product.BRAND_NAME = request.POST['brand']
            product.CATEGORY_NAME = request.POST['category']
            product.MODEL_YEAR = request.POST['model_year']
            product.LIST_PRICE = request.POST['price']
            product.IMAGE_URL = request.POST['image_url']
        else:
            product = Products()
            product.PRODUCT_NAME = request.POST['product_name']
            product.BRAND_NAME = request.POST['brand']
            product.CATEGORY_NAME = request.POST['category']
            product.MODEL_YEAR = request.POST['model_year']
            product.LIST_PRICE = request.POST['price']
            product.IMAGE_URL = request.POST['image_url']
        
        product.save()
        return HttpResponseRedirect(reverse('products'))    
    return render(request, 'product_details.html', {'distinct_brands': distinct_brands,'distinct_categories': distinct_categories,})

def edit_product(request, product_id):
    distinct_brands = Products.objects.values_list('BRAND_NAME', flat=True).distinct()
    distinct_categories = Products.objects.values_list('CATEGORY_NAME', flat=True).distinct()
    product = get_object_or_404(Products, PRODUCT_ID=product_id)
    
    context = {'product':product,'distinct_brands': distinct_brands,'distinct_categories': distinct_categories,}
    return render(request, 'product_details.html', context)

def delete_product(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Products, PRODUCT_ID=product_id)
        Stocks.objects.filter(PRODUCT_ID=product_id).delete()
        Orders.objects.filter(PRODUCT_id = product_id).delete()
        product.delete()
        return redirect('products')

def customers(request):
    custs = Customers.objects.all() 
    
    if request.method == 'POST':
        search_str = request.POST.get('search')
        if(search_str !=''):
            custs = Customers.objects.filter(Q(FIRST_NAME__icontains=search_str) | Q(LAST_NAME__icontains=search_str))
            
    page = request.GET.get('page')
    items_per_page = request.GET.get('items_per_page',10)
    paginator = Paginator(custs, items_per_page)
    try:
        custs = paginator.page(page)
    except PageNotAnInteger:
        custs = paginator.page(1)
    except EmptyPage:
        custs = paginator.page(paginator.num_pages)
    return render(request, 'customers.html', {'customers': custs})

def add_customer(request):
    if request.method == 'POST':
        if 'customer_id' in request.POST and request.POST['customer_id'] != '':
            customer_id = request.POST['customer_id']
            customer = get_object_or_404(Customers, CUSTOMER_ID=customer_id)
            customer.FIRST_NAME = request.POST['first_name']
            customer.LAST_NAME = request.POST['last_name']
            customer.PHONE = request.POST['phone'] if request.POST['phone'] != '' else None
            customer.EMAIL = request.POST['email']
            customer.STREET = request.POST['street'] if request.POST['street'] != '' else None
            customer.CITY = request.POST['city'] if request.POST['city'] != '' else None
            customer.STATE = request.POST['state'] if request.POST['state'] != '' else None
            customer.ZIPCODE = request.POST['zipcode'] if request.POST['zipcode'] != '' else None
        else:
            customer = Customers()
            customer.FIRST_NAME = request.POST['first_name']
            customer.LAST_NAME = request.POST['last_name']
            customer.PHONE = request.POST['phone'] if request.POST['phone'] != '' else None
            customer.EMAIL = request.POST['email']
            customer.STREET = request.POST['street'] if request.POST['street'] != '' else None
            customer.CITY = request.POST['city'] if request.POST['city'] != '' else None
            customer.STATE = request.POST['state'] if request.POST['state'] != '' else None
            customer.ZIPCODE = request.POST['zipcode'] if request.POST['zipcode'] != '' else None
        customer.save()
        return HttpResponseRedirect(reverse('customers'))    
    return render(request, 'customer_details.html')

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customers, CUSTOMER_ID=customer_id)
    
    context = {'customer':customer}
    return render(request, 'customer_details.html', context)

def delete_customer(request, customer_ids):
    if request.method == 'GET':
        customer_ids = customer_ids.split(',')
        for id in customer_ids:
            customer = get_object_or_404(Customers, CUSTOMER_ID=id)
            customer.delete()
        return redirect('customers')
    

