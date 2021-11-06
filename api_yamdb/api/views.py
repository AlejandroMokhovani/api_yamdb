from rest_framework import viewsets, filters, mixins
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from django.core.mail import send_mail

from reviews.models import User

# for api view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .serializers import CreateUserSerializer
from .permissions import IsAdmin


# def create_confirmation_code():
#     return random.randint(100000000000, 999999999999)


# @api_view(['POST'])
# def create_user(request):
#     permission_classes = [IsAdmin]
#
#     if request.method == 'POST':
#
#         print('da')

        # serializer = CreateUserInBaseSerializer(data=request.data)
        # print(request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(viewsets.ModelViewSet):

    # get, post, get single, patch, delete

    queryset = User.objects.all()

    # заменяет url-по-id на url-по-username
    lookup_field = 'username'

    permission_classes = (IsAdmin,)
    serializer_class = CreateUserSerializer

    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)


class SingleUserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):

    """Миксин на получение и редактирование юзера"""
    # get, patch metods
    # any auth user

    permission_classes = (IsAdmin,)
    serializer_class = CreateUserSerializer

    def _get_user(self):
        return get_object_or_404(User, username=self.request.user)

    def get_queryset(self):
        user = self._get_user()
        return User.objects.filter(user=user)


# send_mail(
#     'Тема письма',
#     'Текст письма.',
#     'from@example.com',  # Это поле "От кого"
#     ['to@example.com'],  # Это поле "Кому" (можно указать список адресов)
#     fail_silently=False, # Сообщать об ошибках («молчать ли об ошибках?»)
# )
