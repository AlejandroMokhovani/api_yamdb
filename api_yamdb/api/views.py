from rest_framework import viewsets

from reviews.models import User

from .serializers import UserSerializer, AdminSerializer


class AdminViewSet(viewsets.ModelViewSet):
    pass


class UserViewSet(viewsets.ModelViewSet):
    pass
