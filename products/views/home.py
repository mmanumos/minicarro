from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from ..models.product import Product

# @require_http_methods(["GET"])


def home(request):
    """ Homepage - Products """
    # if user is authenticated redirect to welcome page
    if request.user.is_authenticated:
        products = Product.objects.all().order_by('id')
        context = {
            "products": products
        }
        return render(request, 'home.html', context=context)
    # else redirect to login
    return redirect('/login')
