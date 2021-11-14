from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title, User

from rest_framework.validators import UniqueTogetherValidator


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'bio',
                  'role')
        model = User

        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('email',)),
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('username',))]


class CreateUserInBaseSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username', 'email')
        model = User
        read_only_fields = ('confirmation_code',)

        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('email',)),
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('username',))]


class CreateTokenSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username', 'confirmation_code')
        model = User
        read_only_fields = ('username', )


class UserPatchMeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'bio',
                  'role')
        model = User
        read_only_fields = ('role',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = '__all__'
        read_only_fields = ('id',)

    def rating(self):
        scores = Review.objects.filter(title_id=self.initial_data.id)
        rating = sum(scores.rating) / len(scores.rating)
        return rating


class TitleCreateSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )

    class Meta:
        fields = '__all__'
        model = Title


# Сериализаторы V1
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('id',)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        fields = ('score', 'author')
        model = Review
        read_only_fields = ('id',)
