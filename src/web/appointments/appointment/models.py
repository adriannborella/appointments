from django.db import models
from django.db.models import fields
from django.core.exceptions import ValidationError
from datetime import timedelta, datetime

APPOINTMENT_STATE_CHOICE = [
    ('unassigned', 'Un Assigned'),
    ('assigned', 'Assigned'),
    ('done', 'Done'),
    ('canceled', 'Canceled'),
]

PROCCESS_STATE_CHOICES = [
    ("draft", "Draft"),
    ("done", "Done"),
    ("cancel", "Canel"),
]


class ProccessCreate(models.Model):
    company = models.ForeignKey('company.company', on_delete=models.RESTRICT)
    state = fields.CharField(
        "State", max_length=10, choices=PROCCESS_STATE_CHOICES, default='draft'
    )
    date_start = fields.DateField("Start Date")
    date_until = fields.DateField("Until Date")

    def clean(self) -> None:
        if self.date_start > self.date_until:
            raise ValidationError("The until date must be after the start date.")
        return super().clean()

    def generate_appointments(self, start_date, end_date, duration):
        current_date = start_date
        while current_date < end_date:
            until_date = current_date + timedelta(minutes=duration)
            Appointment.objects.create(
                date_start=current_date, date_until=until_date, create_process=self
            )

            current_date = until_date

    def validate_confirm(self):
        exists_appointment = Appointment.objects.filter(
            date_start__gte=self.date_start, date_until__lte=self.date_until
        )
        if exists_appointment.exists():
            raise ValidationError(
                "There are appointments in this period of time, please select another dates"
            )

    def confirm(self):
        end_date = self.date_start

        while end_date <= self.date_until:
            blocks = self.company.availableblock_set.filter(
                day_of_week=end_date.weekday()
            )
            for record in blocks:
                start_date = datetime.combine(end_date, record.date_start)
                until_date = datetime.combine(end_date, record.date_until)
                self.generate_appointments(
                    start_date, until_date, self.company.appointment_duration
                )

            end_date += timedelta(days=1)

        self.state = 'done'
        self.save()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = 'ProccessCreate'
        verbose_name_plural = 'ProccessCreates'


# Create your models here.
class Appointment(models.Model):
    """Model definition for Appointment."""

    date_start = fields.DateTimeField("Start Date")
    date_until = fields.DateTimeField("Until Date")
    description = fields.TextField("Description", null=True, blank=True)
    state = fields.CharField(
        "State", max_length=25, choices=APPOINTMENT_STATE_CHOICE, default='unassigned'
    )

    archived = fields.BooleanField("Archived", default=False)
    create_process = models.ForeignKey(
        ProccessCreate, on_delete=models.RESTRICT, null=True, blank=True
    )
    customer = models.ForeignKey(
        "customer.customer", on_delete=models.RESTRICT, null=True, blank=True
    )

    class Meta:
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        """Unicode representation of Appointment."""
        return f"{self.id}"
