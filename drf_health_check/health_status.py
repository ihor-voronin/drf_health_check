from .settings import settings


class HealthChecker:
    HEALTH_UP = "UP"
    HEALTH_DOWN = "DOWN"

    ALL_STATUSES = (HEALTH_UP, HEALTH_DOWN)

    @classmethod
    def get_health_status(cls) -> str:
        for health_check in settings.get_providers():
            if not health_check.check():
                return cls.HEALTH_DOWN
        return cls.HEALTH_UP
