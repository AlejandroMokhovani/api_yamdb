from rest_framework import serializers
from reviews.models import User

from rest_framework.validators import UniqueTogetherValidator


class CreateUserSerializer(serializers.ModelSerializer):


    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'bio',
                  'role')
        model = User

        validators = [
                UniqueTogetherValidator(
                    queryset=User.objects.all(),
                    fields=('email',)
                ),
                UniqueTogetherValidator(
                    queryset=User.objects.all(),
                    fields=('username',)
                )
            ]


class CreateUserInBaseSerializer(serializers.ModelSerializer):


    class Meta:
        fields = ('username', 'email')
        model = User

        validators = [
                UniqueTogetherValidator(
                    queryset=User.objects.all(),
                    fields=('email',)
                ),
                UniqueTogetherValidator(
                    queryset=User.objects.all(),
                    fields=('username',)
                )
            ]
