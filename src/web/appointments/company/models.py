from django.db import models
from django.db.models import fields

AVAILABLEBLOCK_DAYOFWEEK_CHOICE = [
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
]


# Create your models here.
class Company(models.Model):
    """Model definition for Company."""

    name = fields.CharField("Name", max_length=100)
    appointment_duration = fields.IntegerField("Appointment Duration", default=0)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Company."""

        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        """Unicode representation of Company."""
        return self.name


class AvailableBlock(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.RESTRICT, verbose_name="Company"
    )
    date_start = fields.TimeField("Start Date")
    date_until = fields.TimeField("Until Date")
    day_of_week = fields.IntegerField(
        "Day of Week", choices=AVAILABLEBLOCK_DAYOFWEEK_CHOICE
    )
    color = fields.CharField("Color", max_length=10, null=True, blank=True)
