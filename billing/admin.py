from django.contrib import admin

from .models import FoodItem, Bill

class FoodItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Bill, admin.ModelAdmin)

