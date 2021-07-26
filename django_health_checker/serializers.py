from rest_framework import serializers

from .providers import HealthCheckProvider


class AnnotateHealthSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=[HealthCheckProvider.ALL_STATUSES])
