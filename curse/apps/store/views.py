from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Products, InstrumentCategories, CustomUser, Orders
from .forms import OrderForm, RegistrationForm
from django.utils import timezone


def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', context={"products": products})


@login_required
def make_order(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    client, created = CustomUser.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.Product = product
            order.Client = client
            order.Client_name = f"{client.username}"
            order.Address = client.Address
            order.Order_Date = timezone.now()  # Set the order date to the current date and time
            order.save()

            messages.success(request, 'Order placed successfully!')
            return redirect('index')  # Redirect to the homepage after submitting the order
    else:
        form = OrderForm()

    return render(request, 'make_order.html', {'product': product, 'form': form})

@login_required(login_url='login')
def orders(request):
    client = get_object_or_404(CustomUser, user=request.user)
    orders = Orders.objects.filter(Client=client)

    # Create a flat list of products associated with orders
    products = [order.Product for order in orders]

    return render(request, 'orders.html', context={"products": products})

def products(request):
    max_price = request.GET.get('price', None)
    category = request.GET.get('category', None)

    filtered_products = Products.objects.all()

    if max_price:
        filtered_products = filtered_products.filter(Price__lte=max_price)

    if category:
        filtered_products = filtered_products.filter(Category=category)

    # Fetch all distinct categories for the filter dropdown
    categories = InstrumentCategories.objects.values_list('Name', flat=True).distinct()

    return render(request, 'products.html', context={
        "filtered_products": filtered_products,
        "categories": categories
    })

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a CustomUser instance and associate it with the new user
            custom_user = CustomUser(user=user)
            custom_user.save()

            auth_login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('index')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})
