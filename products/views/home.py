from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from ..models.product import Product


@require_http_methods(["GET"])
def home(request):
    """ Homepage - Products """
    # if user is not authenticated redirect to login
    if request.user.is_authenticated:
        products = Product.objects.all().order_by('id')
        context = {
            "products": products
        }
        return render(request, 'home.html', context=context)
    # else redirect to login
    return redirect('/login')
