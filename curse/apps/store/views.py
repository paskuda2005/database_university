from django.shortcuts import render
from django.http import HttpResponse
from .models import Products

def index(request):
    products = Products.objects.all()
    print(products)
    return render(request, 'index.html', context={"products": products})
