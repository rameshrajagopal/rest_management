from django import template
from billing.models import FoodItem, Bill
import datetime

register = template.Library()

@register.inclusion_tag('billing/fooditem_list.html')
def get_fooditem_list():
    return {'fitem_list':FoodItem.objects.all()}

@register.inclusion_tag('billing/fooditem_list.html')
def get_top_fooditem_list():
    top_item_list = FoodItem.objects.order_by('-times_ordered')[:5]
    return {'fitem_list': top_item_list}

@register.inclusion_tag('billing/turnover_list.html')
def get_oneweek_sales_info(days=7):
    start_date = datetime.date.today() - datetime.timedelta(days=8)
    end_date = datetime.date.today()- datetime.timedelta(days=1)
    bills = Bill.objects.filter(when__range=[start_date, end_date])
    bills_dict = {}
    for i in range(1, 8):
        run_date = datetime.date.today() - datetime.timedelta(days=i)
        day_wise_bills = bills.filter(when__day=run_date.day)
        total = 0 
        for b in day_wise_bills:
            total += b.total
        bills_dict[run_date] = total
    return {'bills': bills_dict}
      
