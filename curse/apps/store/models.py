from django.db import models


class Client(models.Model):
    ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=50, null=True, blank=True)
    Last_Name = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=255, null=True, blank=True)
    Phone = models.CharField(max_length=15, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"

class InstrumentCategory(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Name

class Manufacturer(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.Name

class Order(models.Model):
    ID = models.AutoField(primary_key=True)
    Client_ID = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    Order_Date = models.DateField(null=True, blank=True)
    Total_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Product_ID = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Order {self.ID}"

class Payment(models.Model):
    ID = models.AutoField(primary_key=True)
    Order_ID = models.ForeignKey(Order, on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Payment_Date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Payment {self.ID}"

class Product(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)
    Manufacturer_ID = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Name

class Sale(models.Model):
    ID = models.AutoField(primary_key=True)
    Product_ID = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    Order_ID = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Sale_Price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Sale {self.ID}"

