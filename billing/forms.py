from __future__ import absolute_import

from django import forms
from .models import BillInfo

class FoodBillInfoForm(forms.ModelForm):
    class Meta:
        fields = ('item', 'quantity', )
        model = BillInfo

class FoodBillForm(FoodBillInfoForm):
    srno  = forms.IntegerField()
    total = forms.FloatField()
    price = forms.FloatField()

    class Meta(FoodBillInfoForm.Meta):
        fields = ('srno',) + FoodBillInfoForm.Meta.fields + ('price', 'total',)
