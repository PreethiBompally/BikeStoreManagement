from django.db import models

class Brands(models.Model):
    BRAND_ID = models.IntegerField(primary_key=True)
    BRAND_NAME = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'brands'

class Categories(models.Model):
    CATEGORY_ID = models.IntegerField(primary_key=True)
    CATEGORY_NAME = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'categories'

class Staffs(models.Model):
    STAFF_ID = models.IntegerField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=50)
    LAST_NAME = models.CharField(max_length=50)
    PHONE = models.BigIntegerField(null=True, blank=True)
    EMAIL = models.CharField(max_length=50, null=True, blank=True)
    ACTIVE = models.IntegerField()
    STORE_ID = models.IntegerField()
    MANAGER_ID = models.IntegerField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'staffs'

class Stores(models.Model):
    STORE_ID = models.IntegerField(primary_key=True)
    STORE_NAME = models.CharField(max_length=50, null=True, blank=True)
    PHONE = models.BigIntegerField(null=True, blank=True)
    EMAIL = models.CharField(max_length=50, null=True, blank=True)
    STREET = models.CharField(max_length=50, null=True, blank=True)
    CITY = models.CharField(max_length=50, null=True, blank=True)
    STATE = models.CharField(max_length=50, null=True, blank=True)
    ZIPCODE = models.IntegerField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'stores'

class Products(models.Model):
    PRODUCT_ID = models.IntegerField(primary_key=True)
    PRODUCT_NAME = models.CharField(max_length=1024, null=True, blank=True)
    BRAND_ID = models.IntegerField()
    CATEGORY_ID = models.IntegerField()
    MODEL_YEAR = models.IntegerField(null=True, blank=True)
    LIST_PRICE = models.DecimalField(max_digits=20, decimal_places=5)
    class Meta:
        managed = False
        db_table = 'products'

class Stocks(models.Model):
    STORE_ID = models.IntegerField(primary_key=True)
    PRODUCT_ID = models.IntegerField()
    QUANTITY = models.DecimalField(max_digits=20, decimal_places=5)
    class Meta:
        managed = False
        db_table = 'stocks'
        unique_together = (('STORE_ID', 'PRODUCT_ID'),)

class Orders(models.Model):
    ORDER_ID = models.IntegerField(primary_key=True)
    CUSTOMER_ID = models.IntegerField()
    ORDER_STATUS = models.IntegerField(null=True, blank=True)
    ORDER_DATE = models.DateTimeField(null=True, blank=True)
    REQUIRED_DATE = models.DateTimeField(null=True, blank=True)
    SHIPPED_DATE = models.DateTimeField(null=True, blank=True)
    STORE_ID = models.IntegerField()
    STAFF_ID = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'orders'

class OrderItems(models.Model):
    ORDER_ID = models.IntegerField(primary_key=True)
    ITEM_ID = models.IntegerField()
    PRODUCT_ID = models.IntegerField()
    QUANTITY = models.DecimalField(max_digits=20, decimal_places=5)
    LIST_PRICE = models.DecimalField(max_digits=20, decimal_places=5)
    DISCOUNT = models.DecimalField(max_digits=20, decimal_places=5)
    class Meta:
        managed = False
        db_table = 'order_items'
        unique_together = (('ORDER_ID', 'ITEM_ID', 'PRODUCT_ID'),)


class Customers(models.Model):
    CUSTOMER_ID = models.IntegerField(primary_key=True)
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