from rest_framework import serializers
from reviews.models import User, Comment, Review


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = User

# сериализаторы v1
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = '__all__'
        model = Review