from django.contrib import admin
from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', "last_name", "document_number")
    # list_filter = ('',)
    fields = [('first_name', "last_name"), ('document_number', "phone")]
    # inlines = [
    #     AppointmentAdminInline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
