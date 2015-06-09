from django.conf.urls import patterns, url
from billing import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name='index'),
        url(r'^foodbill/$', views.food_bill, name='foodbill'),
        url(r'^expensebill/$', views.expense_bill, name='expensebill'),
        url(r'^get_price/$', views.getprice_view, name='getprice'),
        )
