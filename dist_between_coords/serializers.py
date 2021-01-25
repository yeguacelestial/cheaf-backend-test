from rest_framework import serializers


class DistBetweenCoordsSerializer(serializers.Serializer):
    coords = serializers.ListField(
        min_length=2, max_length=2
    )
