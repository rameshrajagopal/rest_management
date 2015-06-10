from django.shortcuts import render
from .forms import FoodBillForm
from .models import FoodItem
from django.http import HttpResponse
from django.forms.formsets import formset_factory

def index(request):
    context = {}
    response = render(request, 'billing/index.html', context)
    return response

def food_bill(request):
    FoodBillFormSet = formset_factory(FoodBillForm, extra=1)
    if request.method == 'POST':
        formset = FoodBillFormSet(request.POST, request.FILES)
        if formset.is_valid():
            pass
        print('post method')
    else:
        formset = FoodBillFormSet()
    context = {'formset': formset}
    response = render(request, 'billing/foodbill.html', context)
    return response

def expense_bill(request):
    context = {}
    response = render(request, 'billing/expensebill.html', context)
    return response

def getprice_view(request):
    item = None
    price = 0
    print(request.GET)
    if request.method == "GET":
        item_code = request.GET['item']
        item = FoodItem.objects.get(id=int(item_code))
        price = item.price
    print(price)
    return HttpResponse(price)
