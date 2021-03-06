from django.conf.urls import patterns, url
from billing import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^foodbill/$', views.food_bill, name='foodbill'),
        url(r'^expensebill/$', views.expense_bill, name='expensebill'),
        url(r'^get_price/$', views.getprice_view, name='getprice'),
        url(r'^suggest_food/$', views.suggest_food_view, name='suggestion'),
        url(r'^reports/$', views.report_view, name='reports'),
        url(r'^reports/sales/today/$', views.todays_sales_view,
            name='today_sales_report'),
        url(r'^reports/sales/week/$', views.weeks_sales_view,
            name='week_sales_report'),
        url(r'^reports/sales/month/$', views.months_sales_view,
            name='month_sales_report'),
        url(r'^reports/sales/overall/$', views.overall_sales_view,
            name='overall_sales_report'),
        url(r'^reports/expenses/today/$', views.todays_expenses_view,
            name='today_expenses_report'),
        url(r'^reports/expenses/week/$', views.weeks_expenses_view,
            name='week_expenses_report'),
        url(r'^reports/expenses/month/$', views.months_expenses_view,
            name='month_expenses_report'),
        url(r'^reports/expenses/overall/$', views.overall_expenses_view,
            name='overall_expenses_report'),
        )
