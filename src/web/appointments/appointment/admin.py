from django.contrib import admin
from django.http.request import HttpRequest
from .models import Appointment, ProccessCreate


@admin.action(description="Confirm")
def create_confirm(modeladmin, request, queryset):
    for record in queryset:
        record.confirm()


@admin.register(ProccessCreate)
class ProccessCreateAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'date_start', 'date_until', 'state')
    list_filter = ('state',)
    actions = [create_confirm]


class AppointmentAdminInline(admin.TabularInline):
    model = Appointment
    list_display = ('state', 'date_start', 'date_until', 'description')
    extra = 0

    def has_change_permission(self, request, obj) -> bool:
        return False

    def has_add_permission(self, request: HttpRequest, obj) -> bool:
        return False

    def has_delete_permission(self, request: HttpRequest, obj) -> bool:
        return False


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_start', 'date_until', 'state', 'customer')
    list_filter = ('id', 'state', 'date_start', 'date_until')
    fields = [('date_start', "date_until"), ('customer', 'state'), ('description')]
    # raw_id_fields = ('',)
    readonly_fields = ['create_process', 'date_start', 'date_until']
    search_fields = ('customer',)
    # date_hierarchy = ''
    # ordering = ('',)
