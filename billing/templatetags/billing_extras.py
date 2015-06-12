from django import template
from billing.models import FoodItem, Bill, BillInfo, GoodsBill, GoodsBillInfo
from django.utils import timezone
from collections import OrderedDict
from billing.utils import MinHeap

register = template.Library()

@register.inclusion_tag('billing/fooditem_list.html')
def get_fooditem_list():
    return {'fitem_list':FoodItem.objects.all()}

@register.inclusion_tag('billing/sales_progress.html')
def get_todays_sales_report():
    today = timezone.now()
    print(timezone.tzinfo)
    print(today.day)
    bills = Bill.objects.filter(when__day=today.day)
    expenses = GoodsBill.objects.filter(when__day=today.day)
    context_dict = {}
    sales_total = 0
    for sale in bills:
        print(sale.id)
        sales_total += sale.total 
    print(sales_total)
    expenses_total = 0
    for expense in expenses:
        expenses_total += expense.total
    context_dict = {'sales' : sales_total, 'expense' : expenses_total}
    return context_dict

@register.inclusion_tag('billing/topitem_list.html')
def get_top_fooditem_list():
    start_date = timezone.now() - timezone.timedelta(days=8)
    end_date = timezone.now()
    bills = BillInfo.objects.filter(bill__when__range=[start_date, end_date])
    heap = MinHeap(7)
    for b in bills:
        heap.add(b.item.name, b.quantity)
    top_item_list = heap.get()
    fitem_dict = {}
    for item in top_item_list:
        fitem_dict[item[0]] = item[1]
    return {'fitem_list': fitem_dict}

@register.inclusion_tag('billing/topitem_list.html')
def get_top_expense_list():
    start_date = timezone.now() - timezone.timedelta(days=8)
    end_date = timezone.now()
    bills = GoodsBillInfo.objects.filter(bill__when__range=[start_date, end_date])
    heap = MinHeap(7)
    for b in bills:
        heap.add(b.item.name, b.quantity)
    top_item_list = heap.get()
    fitem_dict = {}
    for item in top_item_list:
        fitem_dict[item[0]] = item[1]
    return {'fitem_list': fitem_dict}

@register.inclusion_tag('billing/turnover_list.html')
def get_oneweek_sales_info(days=7):
    start_date = timezone.now() - timezone.timedelta(days=8)
    end_date = timezone.now()
    bills = Bill.objects.filter(when__range=[start_date, end_date])
    bills_list = []
    for i in range(8):
        run_date = timezone.now() - timezone.timedelta(days=i)
        day_wise_bills = bills.filter(when__day=run_date.day)
        total = 0 
        for b in day_wise_bills:
            total += b.total
        bills_list.append((run_date, total))
    return {'bills_list': OrderedDict(bills_list)}
      
