from django.contrib import admin
from .models import Customer
from appointment.admin import AppointmentAdminInline


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', "last_name", "document_number")
    # list_filter = ('',)
    fields = [('first_name', "last_name"), ('document_number', "phone")]
    inlines = [
        AppointmentAdminInline,
    ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
