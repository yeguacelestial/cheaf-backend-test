from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from user_crud.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        API Endpoint que permite ver o editar usuarios.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]