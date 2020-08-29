from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Seafood


def seafood(request):
    seafoods = Seafood.objects.all()
    return render(request, 'seafood.html', {'seafoods' : seafoods})


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')

