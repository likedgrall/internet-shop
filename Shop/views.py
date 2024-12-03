from django.shortcuts import render
from .models import *

# Create your views here.

def shop(request):
    snickers = Snickers.objects.all()
    return render(request, './Shop/shop.html', {'snickers':snickers})

def index(request):
    return render(request, './Shop/index.html')

def createOrder(request, product_id):
    snicker = Snickers.objects.get(id=product_id) 
    if request.method == "POST": 
        adress = request.POST['adress']
        Order.objects.create(adress = adress, product = snicker)
    return render(request, './Shop/createOrder.html', {'snickerObject':snicker})

def orders(request):
    order = Order.objects.all()
    
    return render(request, './Shop/orders.html')

def detailSnicker(request, product_id):
    snicker = Snickers.objects.get(id=product_id)
    return render(request, './Shop/detailSnicker.html', {'snickerObject':snicker})

 