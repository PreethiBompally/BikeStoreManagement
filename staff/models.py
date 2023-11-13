from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator, ASCIIUsernameValidator
from django.core import validators
from django.utils.translation import gettext as _

class Stores(models.Model):
    STORE_ID = models.AutoField(primary_key=True)
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

class StaffManager(BaseUserManager):
    def create_user(self, USER_NAME,password, **extra_fields):
        if not USER_NAME:
            raise ValueError('The username field must be set')
        # user_name = self.normalize_email(USER_NAME)
        # extra_fields.pop('last_login', None)
        staff = self.model(USER_NAME=USER_NAME,**extra_fields)
        staff.set_password(password)
        staff.save(using=self._db)
        return staff

    def create_superuser(self, user_name, email, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(user_name = user_name, email = email,**extra_fields)

class Staff(AbstractBaseUser):
    # username_validator = UnicodeUsernameValidator() if hasattr(validators, 'UnicodeUsernameValidator') else ASCIIUsernameValidator()
    USER_NAME = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    STAFF_ID = models.AutoField(primary_key=True)
    FIRST_NAME = models.CharField(max_length=50)
    LAST_NAME = models.CharField(max_length=50)
    PHONE = models.CharField(max_length=14, null=True, blank=True)
    EMAIL = models.CharField(max_length=50, null=True, blank=True)
    STORE = models.ForeignKey('Stores', on_delete=models.CASCADE, default=None, null=True)    
    IMAGE_URL = models.CharField(max_length=1024, null=True, blank=True)
    
    last_login = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'USER_NAME'
    REQUIRED_FIELDS = ['FIRST_NAME', 'LAST_NAME']
    
    objects = StaffManager()
    
    class Meta:
        managed = False
        db_table = 'staff'
        
    def __str__(self):
        return self.USER_NAME

