from rest_framework import serializers
from reviews.models import User


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = User
