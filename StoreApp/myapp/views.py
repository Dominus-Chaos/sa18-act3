from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

def index(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})

def show(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'myapp/show.html', {'product': product})
def product_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def product_show(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/show.html', {'product':product})