from django.apps import AppConfig

from .settings import settings


class HealthChecker(AppConfig):
    name = "health_checker"

    def ready(self) -> None:
        settings.build_settings()
