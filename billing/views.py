from django.shortcuts import render
from .forms import FoodBillForm
from .models import FoodItem, Bill, BillInfo
from django.http import HttpResponse
from django.forms.formsets import formset_factory
from django.utils import timezone
from django.template.defaultfilters import slugify

def index(request):
    context = {}
    response = render(request, 'billing/index.html', context)
    return response

def create_foodbill(total):
    bill = Bill(when=timezone.now(), total=total)
    bill.save()
    return bill

def store_foodbill_info(bill, item):
    fitem_obj = FoodItem.objects.get(slug=slugify(item[0]))
    fitem_obj.times_ordered += 1
    fitem_obj.save()
    print(bill)
    print(item[0], item[1], item[2])
    bill_info = BillInfo(item=fitem_obj, quantity=item[1], bill=bill) 
    bill_info.save()

def food_bill(request):
    FoodBillFormSet = formset_factory(FoodBillForm, extra=1)
    if request.method == 'POST':
        formset = FoodBillFormSet(request.POST, request.FILES)
        if formset.is_valid():
            total = 0
            items = []
            for form in formset:
                if form.cleaned_data['quantity'] != 0:
                    quantity = form.cleaned_data['quantity']
                    price = form.cleaned_data['price']
                    items.append([form.cleaned_data['item'],
                              quantity, price])
                    total += (quantity * price)
            bill = create_foodbill(total)
            for item in items:
                store_foodbill_info(bill, item)
            formset = FoodBillFormSet()
        else:                
            print('form is having errors');
            formset = FoodBillFormSet()
    else:
        formset = FoodBillFormSet()
    context = {'formset': formset}
    response = render(request, 'billing/foodbill.html', context)
    return response

def expense_bill(request):
    context = {}
    response = render(request, 'billing/expensebill.html', context)
    return response

class FoodItemPrice(object):
    _cache = {}
    @staticmethod
    def get_price(item_code):
        if not item_code in FoodItemPrice._cache:
            print("Getting from db" + item_code)
            item = FoodItem.objects.get(id=int(item_code))
            FoodItemPrice._cache[item_code] = item.price
        return FoodItemPrice._cache[item_code]

def getprice_view(request):
    item = None
    price = 0
    print(request.GET)
    if request.method == "GET":
        price = FoodItemPrice.get_price(request.GET['item'])
    return HttpResponse(price)

def get_fooditem_list(max_results=10, starts_with=''):
    fooditem_list = []
    if starts_with:
        item_list = FoodItem.objects.filter(name__istartswith=starts_with)
    if max_results > 0:
        if len(item_list) > max_results:
            item_list = item_list[:max_results]
    return item_list

def suggest_food_view(request):
    item_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    item_list = get_fooditem_list(max_results=10, starts_with=starts_with)
    return render(request, 'billing/fooditem_list.html', {'fitem_list':
                    item_list})
