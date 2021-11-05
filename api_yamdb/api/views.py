from rest_framework import viewsets, filters, mixins
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import User


from .serializers import CreateUserSerializer
from .permissions import IsAdmin


class UsersViewSet(viewsets.ModelViewSet):

    # get, post, get single, patch, delete

    queryset = User.objects.all()

    serializer_class = CreateUserSerializer
    permission_classes = (IsAdmin,)

    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)


class SingleUserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):

    """Миксин на получение и редактирование юзера"""
    # get, patch metods
    # any auth user

    permission_classes = CreateUserSerializer
    serializer_class = (IsAdmin,)

    def _get_user(self):
        return get_object_or_404(User, username=self.request.user)

    def get_queryset(self):
        user = self._get_user()
        return User.objects.filter(user=user)
