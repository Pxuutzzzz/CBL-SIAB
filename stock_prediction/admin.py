from django.contrib import admin
from .models import StockData, Prediction


@admin.register(StockData)
class StockDataAdmin(admin.ModelAdmin):
    list_display = ['date', 'open_price', 'high_price', 'low_price', 'close_price', 'volume']
    list_filter = ['date']
    search_fields = ['date']
    date_hierarchy = 'date'
    ordering = ['-date']


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'predicted_label', 'probability', 'close_price']
    list_filter = ['predicted_label', 'created_at']
    search_fields = ['created_at']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ['predicted_label', 'probability']
        return []
