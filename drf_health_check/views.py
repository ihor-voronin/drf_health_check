from typing import Any

from django.http import HttpRequest
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .health_status import HealthChecker
from .serializers import AnnotateHealthSerializer


class HealthView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(request=None, responses=AnnotateHealthSerializer())
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> Response:
        return Response({"status": HealthChecker.get_health_status()})
