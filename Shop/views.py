from django.shortcuts import render

# Create your views here.

def shop(request):
    return render(request, './Shop/shop.html')

def index(request):
    return render(request, './Shop/index.html')

def createOrder(request):
    return render(request, './Shop/createOrder.html')

def orders(request):
    return render(request, './Shop/orders.html')