from django.contrib import admin

from .models import FoodItem

class FoodItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(FoodItem, FoodItemAdmin)

