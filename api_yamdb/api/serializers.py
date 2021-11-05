from rest_framework import serializers
from reviews.models import User


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = User


class SingleUserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
        model = User


class CreateUserSerializer(serializers.ModelSerializer):



    # валидация username'a
    # def validate_username(self, username):
    #     user = self.context['request'].user
    #     if User.objects.filter(user=user):
    #         raise serializers.ValidationError('username already use')


    # валидация email'a
    # def validate_email(self, email):
    #     email = self.context['request'].user.email



    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
        model = User
