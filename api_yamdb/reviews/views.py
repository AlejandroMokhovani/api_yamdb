from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin)
from api.filters import TitleFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

# from api.pagination import Pagination
from api.permissions import IsAdminOrReadOnly, IsAuthenticatedOrReadOnly
from api.serializers import (CategorySerializer, CommentSerializer,
                             GenreSerializer, ReviewSerializer,
                             TitleSerializer, TitleCreateSerializer)

from .models import Category, Genre, Title


class CustomMixin(ListModelMixin, CreateModelMixin, DestroyModelMixin,
                  viewsets.GenericViewSet):
    pass


class CategoryViewSet(CustomMixin):
    """API для категорий."""
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'

    def retrieve(self, request, slug=None):
        return Response(status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, slug=None):
        return Response(status=status.HTTP_404_NOT_FOUND)

class GenreViewSet(CustomMixin):
    """API для жанров."""
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    """API для произведений."""
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = PageNumberPagination
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    ordering_fields = ('name',)
    ordering = ('name',)

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return TitleCreateSerializer
        return TitleSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        new_queryset = title.reviews.all()
        return new_queryset

    def perform_create(self, serializer):
        get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(user=self.request.user)
        


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        new_queryset = title.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user)