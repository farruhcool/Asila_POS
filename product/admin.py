from django.contrib import admin
from django.utils.safestring import mark_safe

from core import settings
from .models import Category, Product

admin.site.site_header = 'ASILA-POS'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # def time_create(self, obj):
    #     return obj.created_at.strftime("%d-%m-%Y | %H:%M:%S")
    #
    # def time_update(self, obj):
    #     return obj.updated_at.strftime("%d-%m-%Y | %H:%M:%S")
    #
    # time_create.admin_order_field = 'created_at'
    # time_create.short_description = 'Yaratilgan'
    # time_update.admin_order_field = 'updated_at'
    # time_update.short_description = 'Yangilangan'

    list_display = ['id', 'name', 'description', 'is_active', 'parent', 'slug', 'created_at', 'updated_at']
    list_display_links = ['name']
    list_editable = ['description', 'is_active', 'parent', 'slug']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'title',
        'category_field',
        'description',
        'units',
        'is_active',
        'created_at',
        'updated_at',
        'get_image'
    ]
    readonly_fields = ["get_image"]
    list_display_links = ['title']

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="40" height="40">')

    get_image.short_description = "Rasm"
