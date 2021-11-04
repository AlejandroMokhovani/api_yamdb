from rest_framework import filters, viewsets
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from api.permissions import IsAdminOrReadOnly
from api.serializers import (CategorySerializer, GenreSerializer,
                             TitleSerializer)

from .models import Category, Genre, Title


class CustomMixin(ListModelMixin, CreateModelMixin, DestroyModelMixin,
                  viewsets.GenericViewSet):
    pass


class CategoryViewSet(CustomMixin):
    """API для категорий."""
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(CustomMixin):
    """API для жанров."""
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    """API для произведений."""
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    ordering_fields = ('name',)
    ordering = ('name',)
