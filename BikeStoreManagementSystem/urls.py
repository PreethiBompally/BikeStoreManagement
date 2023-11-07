"""BikeStoreManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bikeshop import views
# import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('customers/', views.customers, name='customers'),
    path('brands/', views.brands, name='brands'),
    path('categories/', views.categories, name='categories'),
    path('staffs/', views.staffs, name='staffs'),
    path('stores/', views.stores, name='stores'),
    path('products/', views.products, name='products'),
    path('stocks/', views.stocks, name='stocks'),
    path('orders/', views.orders, name='orders'),
    path('order_items/', views.order_items, name='order_items'),
]
