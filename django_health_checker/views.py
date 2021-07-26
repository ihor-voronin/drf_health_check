from typing import Any

from django.http import HttpRequest, JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .providers import HealthCheckProvider
from .serializers import AnnotateHealthSerializer


class HealthView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(request=None, responses=AnnotateHealthSerializer())
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse:
        return JsonResponse({"status": HealthCheckProvider.get_health_status()})
