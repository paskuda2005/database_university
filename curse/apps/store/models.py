from django.db import models


from django.db import models

class Clients(models.Model):
    ID = models.IntegerField(primary_key=True)
    First_Name = models.CharField(max_length=50, null=True, blank=True)
    Last_Name = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=255, null=True, blank=True)
    Phone = models.CharField(max_length=15, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'clients'

class InstrumentCategories(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'instrument_categories'

class Manufacturers(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'manufacturers'

class Orders(models.Model):
    ID = models.IntegerField(primary_key=True)
    Client_ID = models.IntegerField(null=True, blank=True, db_column='Client_ID')
    Order_Date = models.DateField(null=True, blank=True)
    Total_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Product_ID = models.IntegerField(null=True, blank=True, db_column='Product_ID')

    class Meta:
        db_table = 'orders'

class Payments(models.Model):
    ID = models.IntegerField(primary_key=True)
    Order_ID = models.IntegerField(null=True, blank=True, db_column='Order_ID')
    Amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Payment_Date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'payments'

class Products(models.Model):
    ID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)
    Manufacturer_ID = models.IntegerField(null=True, blank=True, db_column='Manufacturer_ID')
    Image_url = models.TextField(max_length=2000, blank=True, db_column='image_url')

    class Meta:
        db_table = 'products'

class Sales(models.Model):
    ID = models.IntegerField(primary_key=True)
    Product_ID = models.IntegerField(null=True, blank=True, db_column='Product_ID')
    Order_ID = models.IntegerField(null=True, blank=True, db_column='Order_ID')
    Quantity = models.IntegerField(null=True, blank=True)
    Sale_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'sales'


