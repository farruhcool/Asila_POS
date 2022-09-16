from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Departament, Role, Employee


@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ['dep_id', 'name', 'created_at', 'updated_at', 'is_active']
    list_editable = ['is_active']
    list_display_links = ['name']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at', 'is_active']
    list_editable = ['is_active']
    list_display_links = ['name']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'dept',
        'em_role',
        'birth_day',
        'hire_date',
        'is_active',
        'get_image']
    list_display_links = ['full_name']
    # list_editable = ['is_active']
    readonly_fields = ("get_image", "created_at", "updated_at")
    fieldsets = (
        ("FIO", {
            "fields": (('full_name',),)
        }),
        ("Shaxsiy ma'lumotlar", {
            "fields": (('passport', 'birth_day'), ('gender', 'address'),)
        }),
        ("Holat", {
            "fields": (('hire_date',), ('is_active',),)
        }),
        ("Bo'lim", {
            "fields": (('dept', 'em_role'),)
        }),
        ("Sanalar", {
            "fields": (('created_at',), ('updated_at',),)
        }),
        ("Rasm", {
            "classes": ("collapse",),
            "fields": (('image', 'get_image'),)
        }),

    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="30" height="30">')

    get_image.short_description = "Rasm"
