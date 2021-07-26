import logging
from typing import Set, Type

from django_health_checker.settings import settings

log = logging.getLogger(__name__)


class HealthCheckProvider:
    name: str

    HEALTH_UP = "UP"
    HEALTH_DOWN = "DOWN"

    ALL_STATUSES = (HEALTH_UP, HEALTH_DOWN)

    @classmethod
    def _check(cls) -> None:
        raise NotImplementedError()

    @classmethod
    def _restricted_health_checks_classes(cls) -> Set[Type["HealthCheckProvider"]]:
        available_health_checkers = set()
        for health_checker in cls.__subclasses__():
            if health_checker.name in settings.get_provider_names():
                available_health_checkers.add(health_checker)
        return available_health_checkers

    @classmethod
    def check(cls) -> bool:
        try:
            cls._check()
            return True
        except Exception as ex:
            log.error(f"check {cls.__class__.__name__} failed with {ex}")
            return False

    @classmethod
    def get_health_status(cls) -> str:
        for health_check in cls._restricted_health_checks_classes():
            if not health_check.check():
                return cls.HEALTH_DOWN
        return cls.HEALTH_UP
