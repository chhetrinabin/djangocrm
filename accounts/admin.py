from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('name', 'email', 'phone',)


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'category',
        'description',
        'date_created',
    )
    list_filter = ('date_created',)
    raw_id_fields = ('tags',)
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'customer',  'status', 'product', 'date_created',)
    list_filter = ('customer', 'product', 'date_created')
    list_editable = ('status',)
