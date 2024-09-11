from rest_framework import routers
from django.urls import include, path
from .api import AppointmentViewSet

router = routers.DefaultRouter()
router.register('appointment', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
