__all__ = ["settings"]

from typing import Any, ClassVar, Optional, Set

from django.conf import settings as django_settings
from django.utils.module_loading import import_string

from .providers import HealthCheckProvider


class Settings:
    __providers: ClassVar[Set[HealthCheckProvider]] = set()

    @staticmethod
    def _get_from_django_settings(
        s: Any, key: str, default: Optional[Any] = None
    ) -> Any:
        return getattr(
            s, key, getattr(s, key.lower(), getattr(s, key.upper(), default))
        )

    @classmethod
    def build_settings(cls) -> None:
        provider_names = set(
            cls._get_from_django_settings(
                django_settings, "HEALTH_CHECK_PROVIDERS", set()
            )
        )
        cls.__providers = {
            import_string(provider_name) for provider_name in provider_names
        }

    @classmethod
    def get_providers(cls) -> Set[HealthCheckProvider]:
        return cls.__providers


settings = Settings()
