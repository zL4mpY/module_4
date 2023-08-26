from django.contrib import admin
from django.utils.html import format_html, mark_safe
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'description', 'price', 'created_date', 'updated_date', 'auction', 'user', 'show_thumbnail']
    list_filter = ['auction', 'created_at', 'updated_at']

    actions = ['make_auction_as_false', 'make_auction_as_true']
    
    fieldsets = (
        ('Общее', {'fields': ('title', 'user', 'description', 'image')}),
        ('Финансы', {'fields': ('price', 'auction'), 'classes': ['collapse']})
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)
