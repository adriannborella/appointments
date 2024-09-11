from rest_framework.viewsets import ModelViewSet
from .models import Appointment
from .serializer import AppointmentSerializer


class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
