import pizza
from pizzaApp.models import *
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'pizzaApp/index.html', context)


def order(request, pk):
    order = Order.objects.get(id=pk)
    pizzas = order.pizzas.all()
    context = {'order': order, 'pizzas': pizzas}
    return render(request, 'pizzaApp/order.html', context)


def pizza(request, pk):
    pizza = Pizza.objects.get(id=pk)
    ingredients = pizza.ingredients.all()
    context = {'ingredients': ingredients}
    return render(request, 'pizzaApp/pizza.html', context)
