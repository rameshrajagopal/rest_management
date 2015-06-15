from django.contrib import admin

from .models import FoodItem, Bill, Goods, GoodsBill, BillInfo, GoodsBillInfo

class FoodItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class GoodsItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Bill, admin.ModelAdmin)
admin.site.register(Goods, GoodsItemAdmin)
admin.site.register(GoodsBill, admin.ModelAdmin)
admin.site.register(BillInfo, admin.ModelAdmin)
admin.site.register(GoodsBillInfo, admin.ModelAdmin)

