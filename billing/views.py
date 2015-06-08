from django.shortcuts import render
from .forms import FoodBillForm

def index(request):
    context = {}
    response = render(request, 'billing/index.html', context)
    return response

def food_bill(request):
    form = FoodBillForm()
    context = {'form': form}
    response = render(request, 'billing/foodbill.html', context)
    return response

def expense_bill(request):
    context = {}
    response = render(request, 'billing/expensebill.html', context)
    return response


