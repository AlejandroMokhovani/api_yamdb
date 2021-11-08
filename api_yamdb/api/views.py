from rest_framework import viewsets, filters, mixins
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from django.core.mail import send_mail

from rest_framework_simplejwt.tokens import RefreshToken

from reviews.models import User

<<<<<<< HEAD
=======
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_pmake_password для одного значения генериру


import random

>>>>>>> auth_and_users
# for api view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


<<<<<<< HEAD
from .serializers import CreateUserSerializer
from .permissions import IsAdmin


# def create_confirmation_code():
#     return random.randint(100000000000, 999999999999)
=======
from .serializers import (
    CreateUserSerializer,
    CreateUserInBaseSerializer,
    CreateTokenSerializer
)

from .permissions import IsAdmin


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'access': str(refresh.access_token)
    }

def send_mail_with_code(confirmation_code, email):
    send_mail(
        'Код регистрации',
        f'{confirmation_code}',
        'api_yamdb@mail.com',
        [f'{email}'],
        fail_silently=False,
    )


@api_view(['POST'])
def create_user(request):

    if request.method == 'POST':

        serializer = CreateUserInBaseSerializer(data=request.data)

        email = request.data['email']
        confirmation_code = get_random_string(10)

        code = hash(confirmation_code)
>>>>>>> auth_and_users

        request.data.update({'confirmation_code': code})


        if serializer.is_valid():
            serializer.save()
            send_mail_with_code(confirmation_code, email)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_token(request):

    if request.method == 'POST':
        #
        serializer = CreateTokenSerializer(data=request.data)

        request_code = hash(request.data['confirmation_code'])

        user = User.objects.get(username=request.data['username'])
        user_code = user.confirmation_code

        print(user.confirmation_code)

        if True:
            token = get_tokens_for_user(user)
            return Response(token, status=status.HTTP_200_OK)
        else:
            print('failed')




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
