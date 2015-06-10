from __future__ import absolute_import

from django import forms
from .models import BillInfo, GoodsExpense

class FoodBillInfoForm(forms.ModelForm):
    class Meta:
        fields = ('item', 'quantity', )
        model = BillInfo

class FoodBillForm(FoodBillInfoForm):
    price = forms.FloatField(widget=forms.HiddenInput())

    class Meta(FoodBillInfoForm.Meta):
        fields = FoodBillInfoForm.Meta.fields + ('price',)

class GoodExpenseBillForm(forms.ModelForm):

    class Meta:
        fields = ('name', 'category', 'quantity', 'price',) 
        model = GoodsExpense

