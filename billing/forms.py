from __future__ import absolute_import

from django import forms
from .models import BillInfo, GoodsBillInfo, FoodItem

class FoodBillInfoForm(forms.ModelForm):
    item = forms.ModelChoiceField(queryset=FoodItem.objects.all(), label='')
    quantity = forms.FloatField(label='')
    class Meta:
        fields = ('item', 'quantity', )
        model = BillInfo

class FoodBillForm(FoodBillInfoForm):
    price = forms.FloatField(widget=forms.HiddenInput())

    class Meta(FoodBillInfoForm.Meta):
        fields = FoodBillInfoForm.Meta.fields + ('price',)

class GoodsBillForm(forms.ModelForm):
    price = forms.FloatField()

    class Meta:
        fields = ('item', 'quantity', 'price',)
        model = GoodsBillInfo



