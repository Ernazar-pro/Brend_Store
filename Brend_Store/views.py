from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    return render(
        request,
        'base.html',
    )

def about(request):
    return render(
        request,
        'Brend_Store/about.html',
    )

def contact(request):
    return render(
        request,
        'Brend_Store/contact.html',
    )

def products(request):
    product = Product.objects.all()
    context = {
        'products': product
    }
    return render(request,'Brend_Store/products.html',context)

