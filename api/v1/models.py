from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# User Roles Master
class Role(models.Model):
    ADMIN = 1
    PRODUCTION = 2
    USER = 3
    ROLE_CHOICES = [(ADMIN, 'ADMIN'),(PRODUCTION, 'PRODUCTION'),(USER, 'USER'),]
    role = models.CharField(max_length=20,null=False, choices=ROLE_CHOICES,)

    class Meta:
        db_table = "UserRoles"

    def __str__(self):
        return self.role

# Country Master
class CountryMaster(models.Model):
    country_name = models.CharField(max_length=100,null=True,blank=True)
    country_code = models.IntegerField(null=True,blank=True)
    country_flag = models.ImageField(upload_to='country_flag/',null=True,blank=True)
    currency = models.CharField(max_length=50,null=True,blank=True)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "CountryMaster"
        indexes = [
            models.Index(fields=['country_name','country_code']),
        ]



#User Master
class UserMaster(AbstractUser):
    full_name = models.CharField(max_length=250,null=True,blank=True)
    username = models.CharField(max_length=250,null=True,blank=True)
    email = models.EmailField(max_length=500,null=True, blank=True,unique=True)
    mobile_number = models.CharField(max_length=16,null=True,blank=True,unique=True)
    roles = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    raw_password = models.CharField(max_length=100, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_logged_in=models.BooleanField(default=False)
    is_mobile_verfied = models.BooleanField(default=False)
    is_email_verfied = models.BooleanField(default=False)
    mobile_otp =  models.CharField(max_length=4, null=True, blank=True)
    email_otp =  models.CharField(max_length=4, null=True, blank=True)
    mobile_otp_generate_time = models.DateTimeField( blank=True,null=True)
    email_otp_generate_time = models.DateTimeField( blank=True,null=True)
    
    
    
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_by = models.CharField(max_length=100,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "UserMaster"
        indexes = [
            models.Index(fields=['email','mobile_number']),
        ]
        