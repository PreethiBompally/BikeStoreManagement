from django.db import models
from django.utils.translation import gettext as _

class Products(models.Model):
    PRODUCT_ID = models.AutoField(primary_key=True)
    PRODUCT_NAME = models.CharField(max_length=1024, null=True, blank=True)
    BRAND_NAME = models.CharField(max_length=1024, null=True, blank=True)
    CATEGORY_NAME = models.CharField(max_length=1024, null=True, blank=True)
    MODEL_YEAR = models.IntegerField(null=True, blank=True)
    LIST_PRICE = models.DecimalField(max_digits=20, decimal_places=5)
    IMAGE_URL = models.CharField(max_length=1024, null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'products'

class Stocks(models.Model):
    STORE_ID = models.ForeignKey('staff.Stores', on_delete=models.CASCADE)
    PRODUCT_ID = models.ForeignKey('Products', on_delete=models.CASCADE)
    QUANTITY = models.DecimalField(max_digits=20, decimal_places=5)
    class Meta:
        managed = False
        db_table = 'stocks'
        unique_together = (('STORE_ID', 'PRODUCT_ID'),)

class Orders(models.Model):
    ORDER_ID = models.AutoField(primary_key=True)
    CUSTOMER_ID = models.ForeignKey('Customers', on_delete=models.CASCADE)
    ORDER_DATE = models.DateTimeField(null=True, blank=True)
    REQUIRED_DATE = models.DateTimeField(null=True, blank=True)
    SHIPPED_DATE = models.DateTimeField(null=True, blank=True)
    STORE_ID = models.ForeignKey('staff.Stores', on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'orders'
class Customers(models.Model):
    CUSTOMER_ID = models.AutoField(primary_key=True)
    FIRST_NAME = models.CharField(null = False, max_length=50)
    LAST_NAME = models.CharField(null = False, max_length=50)
    PHONE = models.TextField(null = True, blank=True)
    EMAIL = models.CharField(max_length=50, null = True, blank=True)
    STREET = models.CharField(max_length=50, null = True, blank=True)
    CITY = models.CharField(max_length=50, null = True, blank=True)
    STATE = models.CharField(max_length=50, null = True, blank=True)
    ZIPCODE = models.IntegerField(null = True, blank=True)
    
    class Meta:
        managed = False
        db_table = 'customers'        