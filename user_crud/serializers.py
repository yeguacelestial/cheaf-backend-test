from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'date_joined']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'date_joined': {
                'read_only': True
            }
        }