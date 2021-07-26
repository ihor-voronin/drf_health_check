from django.db import connection

from .base import HealthCheckProvider


class DBHealthCheckProvider(HealthCheckProvider):
    @classmethod
    def _check(cls) -> None:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
