from rest_framework import serializers

from .health_status import HealthChecker


class AnnotateHealthSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=[HealthChecker.ALL_STATUSES])
