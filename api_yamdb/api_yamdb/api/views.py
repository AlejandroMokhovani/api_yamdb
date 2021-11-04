from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from reviews.models import User, Review, Comment, Title


from .serializers import UserSerializer, AdminSerializer, CommentSerializer, ReviewSerializer


class AdminViewSet(viewsets.ModelViewSet):
    pass


class UserViewSet(viewsets.ModelViewSet):
    pass

