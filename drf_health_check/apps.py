from django.apps import AppConfig

from .settings import settings


class DRFHealthCheck(AppConfig):
    name = "drf_health_check"

    def ready(self) -> None:
        settings.build_settings()
