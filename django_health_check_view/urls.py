from django.urls import path

from .views import HealthView

app_name = "health_check"

urlpatterns = [
    path("", HealthView.as_view(), name="health_check_status"),
]
