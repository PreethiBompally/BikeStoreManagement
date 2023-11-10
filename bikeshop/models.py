from django.db import models

class Staff(models.Model):
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
        db_table = 'staff'

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
    BRAND_NAME = models.CharField(max_length=1024, null=True, blank=True)
    CATEGORY_NAME = models.CharField(max_length=1024, null=True, blank=True)
    MODEL_YEAR = models.IntegerField(null=True, blank=True)
    LIST_PRICE = models.DecimalField(max_digits=20, decimal_places=5)
    IMAGE_URL = models.CharField(max_length=1024, null=True, blank=True)
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

class Login(models.Model):
    USER_NAME = models.CharField(max_length=255,primary_key=True)  # Add the max_length attribute here
    PASSWORD = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'users'

        