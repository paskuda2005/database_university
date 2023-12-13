from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission
from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    Address = models.CharField(max_length=255, null=True, blank=True)
    Phone = models.CharField(max_length=15, null=True, blank=True)
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = CustomUserManager()

CustomUser._meta.get_field('groups').remote_field.related_name = 'notyuser_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'notyuser_user_permissions'

class InstrumentCategories(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)

class Manufacturers(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=50, null=True, blank=True)

class Products(models.Model):
    Name = models.CharField(max_length=255, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)
    Manufacturer = models.ForeignKey(Manufacturers, on_delete=models.SET_NULL, null=True, blank=True)
    Image_url = models.TextField(max_length=2000, blank=True)

class Orders(models.Model):
    Client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    Order_Date = models.DateField(null=True, blank=True)
    Total_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    Client_name = models.CharField(max_length=255, null=True, blank=True)
    Address = models.CharField(max_length=255, null=True, blank=True)

class Payments(models.Model):
    Order = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True, blank=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Payment_Date = models.DateField(null=True, blank=True)

class Sales(models.Model):
    Product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    Order = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Sale_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
