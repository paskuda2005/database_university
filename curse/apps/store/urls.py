from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('make_order/<int:product_id>/', views.make_order, name='make_order'),
]
