from rest_framework import serializers


class HistorySerializer(serializers.Serializer):
    """Base serializer that includes modified timestamp."""

    modified = serializers.DateTimeField(read_only=True)

