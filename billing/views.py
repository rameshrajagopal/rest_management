from django.shortcuts import render
from .forms import FoodBillForm, GoodsBillForm
from .models import FoodItem, Bill, BillInfo, Goods, GoodsBill, GoodsBillInfo
from django.http import HttpResponse
from django.forms.formsets import formset_factory
from django.utils import timezone
from django.template.defaultfilters import slugify
from billing.utils import get_todays_report, get_weeks_report, get_months_report, get_overall_report
from billing.templatetags.billing_extras import get_sales_info, get_expenses_info

def index(request):
    context = {}
    response = render(request, 'billing/index.html', context)
    return response

def create_foodbill(total):
    print("Bill of ", total, timezone.now())
    bill = Bill(when=timezone.now(), total=total)
    bill.save()
    return bill

def create_goodsbill(total):
    print("creating goods bill of total: {}".format(total))
    bill = GoodsBill(when=timezone.now(), total=total)
    bill.save()
    return bill

def store_foodbill_info(bill, item):
    fitem_obj = FoodItem.objects.get(slug=slugify(item[0]))
    fitem_obj.times_ordered += item[1]
    fitem_obj.save()
    print(bill)
    print(item[0], item[1], item[2])
    bill_info = BillInfo(item=fitem_obj, quantity=item[1], bill=bill)
    bill_info.save()

def store_goodsbill_info(bill, name, quantity, price):
    fitem_obj = Goods.objects.get(slug=slugify(name))
    fitem_obj.price = price
    fitem_obj.save()
    bill_info = GoodsBillInfo(item=fitem_obj, quantity=quantity, bill=bill)
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
            print(formset.errors)
            formset = FoodBillFormSet()
    else:
        formset = FoodBillFormSet()
    context = {'formset': formset}
    response = render(request, 'billing/foodbill.html', context)
    return response

def expense_bill(request):
    GoodsFormSet = formset_factory(GoodsBillForm, extra=1)
    if request.method == 'POST':
        formset = GoodsFormSet(request.POST, request.FILES)
        if formset.is_valid():
            total = 0
            items = []
            for form in formset:
                if form.cleaned_data['quantity'] != 0:
                    name = form.cleaned_data['item']
                    quantity = form.cleaned_data['quantity']
                    price = form.cleaned_data['price']
                    items.append([name, quantity, price])
                    total += (quantity * price)
            bill = create_goodsbill(total)
            for item in items:
                print(item[0], item[1], item[2])
                store_goodsbill_info(bill, item[0], item[1], item[2])
            formset = GoodsFormSet()
        else:
            print(formset.errors)
            formset = GoodsFormSet()
    else:
        formset = GoodsFormSet()
    context = {'formset': formset}
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

def report_view(request):
    (bills_list, sale_total) = get_sales_info(days=7)
    (expense_list, exp_total) = get_expenses_info(days=7)
    return render(request, 'billing/billing_report.html', {'bills_list':
            bills_list, 'expense_list' : expense_list, 'sale_total':
            sale_total, 'exp_total' : exp_total})

def todays_sales_view(request):
    fitems_info = get_todays_report(BillInfo)
    (bills_list, total) = get_sales_info(days=1)
    return render(request, 'billing/fooditem_sales.html', {'fitems_info':
            fitems_info, 'page_header': "Today's sales", 'title':'Today',
            'bills_list': bills_list})

def weeks_sales_view(request):
    fitems_info = get_weeks_report(BillInfo)
    (bills_list, total) = get_sales_info(days=7)
    return render(request, 'billing/fooditem_sales.html', {'fitems_info':
            fitems_info, 'page_header' : "Week's sales", 'title' : 'Week',
            'bills_list': bills_list})

def months_sales_view(request):
    fitems_info = get_months_report(BillInfo)
    (bills_list, total) = get_sales_info(days=31)
    return render(request, 'billing/fooditem_sales.html', {'fitems_info':
            fitems_info, 'page_header' : "Month's sales", 'title': 'Month',
            'bills_list' : bills_list})

def overall_sales_view(request):
    fitems_info = get_overall_report(BillInfo)
    (bills_list, total) = get_sales_info(days=356)
    return render(request, 'billing/fooditem_sales.html', {'fitems_info':
            fitems_info, 'page_header' : "Overall sales", 'title': 'Overall',
            'bills_list' : bills_list})

def todays_expenses_view(request):
    goods_info = get_todays_report(GoodsBillInfo)
    (bills_list, total) = get_expenses_info(days=1)
    return render(request, 'billing/goods_expenses.html', {'goods_info':
            goods_info, 'page_header': "Today's expenses", 'title':'Today',
            'bills_list' : bills_list})

def weeks_expenses_view(request):
    goods_info = get_weeks_report(GoodsBillInfo)
    (bills_list, total) = get_expenses_info(days=7)
    return render(request, 'billing/goods_expenses.html', {'goods_info':
            goods_info, 'page_header' : "Week's expenses", 'title' : 'Week',
            'bills_list' : bills_list})

def months_expenses_view(request):
    goods_info = get_months_report(GoodsBillInfo)
    (bills_list, total) = get_expenses_info(days=31)
    return render(request, 'billing/goods_expenses.html', {'goods_info':
            goods_info, 'page_header' : "Month's expenses", 'title': 'Month',
            'bills_list' : bills_list})

def overall_expenses_view(request):
    goods_info = get_overall_report(GoodsBillInfo)
    (bills_list, total) = get_expenses_info(days=356)
    return render(request, 'billing/goods_expenses.html', {'goods_info':
            goods_info, 'page_header' : "Overall expenses", 'title': 'Overall',
            'bills_list' : bills_list})
