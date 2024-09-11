from django.contrib import admin
from .models import Company, AvailableBlock


# @admin.register(AvailableBlock)
class AvailableBlockAdminInLine(admin.TabularInline):
    model = AvailableBlock
    list_display = ('day_of_week', 'date_start', 'date_until')
    extra = 1


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [AvailableBlockAdminInLine]
