from django.apps import AppConfig

from .settings import settings


class HealthCheck(AppConfig):
    name = "health_check"

    def ready(self) -> None:
        settings.build_settings()
        from . import providers
