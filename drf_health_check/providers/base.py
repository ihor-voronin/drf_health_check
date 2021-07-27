import logging

log = logging.getLogger(__name__)


class HealthCheckProvider:
    @classmethod
    def _check(cls) -> None:
        raise NotImplementedError()

    @classmethod
    def check(cls) -> bool:
        try:
            cls._check()
            return True
        except Exception as ex:
            log.info(f"check {cls.__class__.__name__} failed with {ex}")
            return False
