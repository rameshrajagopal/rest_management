from __future__ import absolute_import

from django import forms
from .models import BillInfo, GoodsBillInfo

class FoodBillInfoForm(forms.ModelForm):
    class Meta:
        fields = ('item', 'quantity', )
        model = BillInfo

class FoodBillForm(FoodBillInfoForm):
    price = forms.FloatField(widget=forms.HiddenInput())

    class Meta(FoodBillInfoForm.Meta):
        fields = FoodBillInfoForm.Meta.fields + ('price',)

class GoodsBillForm(forms.ModelForm):
    price = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        fields = ('item', 'quantity', 'price',)
        model = GoodsBillInfo



