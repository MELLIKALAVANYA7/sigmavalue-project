from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('final_location', 'year', 'city', 'total_carpet_area', 'flat_total', 'shop_total', 'office_total', 'others_total')
    readonly_fields = ('extra_data',)  # If using extra_data for dynamic columns

