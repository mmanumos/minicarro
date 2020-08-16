"""minicarro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views.login import login, register, logout
from products.views.home import home
from products.views.orders import create_order, orders, view_order, pay_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('create_order/', create_order, name='create_order'),
    path('orders/', orders, name='orders'),
    path('view_order/<int:id>', view_order, name='view_order'),
    path('pay_order/', pay_order, name='pay_order'),
]
