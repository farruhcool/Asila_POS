from django.contrib import admin

from .models import Supplier, SupplyBill, SupplyItem, Stock


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'stir', 'phone', 'address', 'email']


class SupplyItemInline(admin.TabularInline):
    model = SupplyItem
    fk_name = 'bill_no'
    extra = 1


@admin.register(SupplyBill)
class SupplyBillAdmin(admin.ModelAdmin):
    list_display = ['bill_no', 'sup_supplier', 'time', 'get_total_price']
    inlines = [SupplyItemInline]


@admin.register(SupplyItem)
class SupplyItemAdmin(admin.ModelAdmin):
    list_display = ['bill_no', 'sup_product', 'quantity', 'per_price', 'total_price']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'supply', 'sup_qty', 'sale', 'sale_qty', 'total_bal_qty']
