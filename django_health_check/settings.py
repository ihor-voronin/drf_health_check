__all__ = ["settings"]

from typing import Any, ClassVar, Optional, Set


class Settings:
    __debug: ClassVar[bool] = False
    __provider_names: ClassVar[Set[str]] = set()

    @staticmethod
    def _get_from_django_settings(
        s: Any, key: str, default: Optional[Any] = None
    ) -> Any:
        return getattr(
            s, key, getattr(s, key.lower(), getattr(s, key.upper(), default))
        )

    @classmethod
    def build_settings(cls) -> None:
        from django.conf import settings as django_settings

        cls.__debug = cls._get_from_django_settings(django_settings, "DEBUG", False)
        cls.__provider_names = cls._get_from_django_settings(
            django_settings, "HEALTH_CHECK_PROVIDERS", set()
        )

    @classmethod
    def get_provider_names(cls) -> Set[str]:
        return cls.__provider_names


settings = Settings()
