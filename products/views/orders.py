from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
import json
from ..models.product import Product
from ..models.order import Order, OrderItems


@require_http_methods(["POST"])
def create_order(request):
    """ View to create an order """
    # get data
    try:
        data = request.POST
        data = list(data.keys())[0]
        data = json.loads(data)
        # create order
        my_order = Order()
        my_order.user_id = request.user
        my_order.status = 0
        my_order.save()
        # order items associated
        for product in data['list_order']:
            order_item = OrderItems()
            order_item.order_id = my_order
            order_item.product_id = Product.objects.get(id=product[0])
            order_item.cant = product[1]
            order_item.save()
        return JsonResponse({"status": "success", "order_id": my_order.id})
    except Exception:
        return JsonResponse({"status": "error"})


@require_http_methods(["GET"])
def orders(request):
    """ View to get all orders by user """
    # if user is not authenticated redirect to login
    if request.user.is_authenticated:
        orders = Order.objects.filter(user_id=request.user).order_by('id')
        context = {
            "orders": orders
        }
        return render(request, 'orders.html', context=context)
    # redirect to login
    return redirect('/login')


@require_http_methods(["GET"])
def view_order(request, id):
    """ View order by id """
    # if user is not authenticated redirect to login
    if request.user.is_authenticated:
        my_order = Order.objects.get(id=id)
        context = {
            "my_order": my_order
        }
        return render(request, 'view_order.html', context=context)
    # redirect to login
    return redirect('/login')


@require_http_methods(["POST"])
def pay_order(request):
    """ Pay order by id """
    # if user is not authenticated redirect to login
    if request.user.is_authenticated:
        try:
            data = request.POST
            data = list(data.keys())[0]
            data = json.loads(data)
            my_order = Order.objects.get(id=data['id'])
            # change status
            my_order.status = 1
            my_order.save()
            return JsonResponse({"status": "success", "order_id": my_order.id})
        except Exception:
            return JsonResponse({"error": "error"})
    # redirect to login
    return redirect('/login')
