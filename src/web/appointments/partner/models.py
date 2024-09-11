from django.db import models
from django.db.models import fields


class Partner(models.Model):
    first_name = fields.CharField("First Name", max_length=200)
    last_name = fields.CharField("Last Name", max_length=60)
    phone = fields.CharField("Phone Number", max_length=50, null=True, blank=True)
    document_number = fields.CharField(
        "document Number", max_length=50, null=True, blank=True
    )

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return f"{self.id} - {self.last_name}, {self.first_name}"
