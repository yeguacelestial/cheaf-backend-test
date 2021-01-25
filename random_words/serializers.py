from rest_framework import serializers


class RandomWordsSerializer(serializers.Serializer):
    words = serializers.ListField(
        child=serializers.CharField(), min_length=10, max_length=10
    )