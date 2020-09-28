from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Seafood, Fruits, Veg, HomeProducts


def search(query=None):
    query_set = []
    queries = query.split(" ")
    for q in queries:
        posts = Product.objects.filter(
            name__icontains=q
        ).distinct()
        for post in posts:
            query_set.append(post)
    return list(set(query_set))


def search2(query=None):
    query_set = []
    queries = query.split(" ")
    for q in queries:
        posts = Fruits.objects.filter(
            name__icontains=q
        ).distinct()
        for post in posts:
            query_set.append(post)
    return list(set(query_set))


def about_us(request):
    products = HomeProducts.objects.all()
    return render(request, 'about_us.html', {'products': products})


def fruit(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    fruits = search2(query)
    context["fruits"] = fruits
    return render(request, 'fruit.html', context)


def seafood(request):
    seafoods = Seafood.objects.all()
    return render(request, 'seafood.html', {'seafoods': seafoods})


def index(request):
    context = {}
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)
    products = search(query)
    context["products"] = products
    return render(request, 'index.html', context)


def veg(request):
    vegies = Veg.objects.all()
    return render(request, 'veg.html', {'vegies': vegies})


def home_view(request):
    return render(request, 'about_us.html')
