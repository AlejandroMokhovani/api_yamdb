from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q

from django.core.exceptions import ValidationError


class User(AbstractUser):
    email = models.EmailField('email', max_length=254, blank=False)
    USER = 'USR'
    MODERATOR = 'MDR'
    ADMIN = 'ADM'
    ROLE_CHOICES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]
    role = models.CharField(
        'role',
        max_length=3,
        choices=ROLE_CHOICES,
        default=USER,
    )
    bio = models.TextField('biography', blank=True)

    class Meta:
        constraints = [
            # юзер должен быть уникальным
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_user'
            ),
            # username юзера не должен быть 'me'
            models.CheckConstraint(
                check=~Q(username__iexact='me'),
                name='cant_given_username'
            ),
        ]


class Category(models.Model):
    name = models.CharField(max_length=256, db_index=True,
                            verbose_name='Название категории',
                            help_text='Укажите название для категории')
    slug = models.SlugField(max_length=256, unique=True,
                            verbose_name='Slug для категории',
                            help_text='Задайте уникальный Slug категории.')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256, db_index=True,
                            verbose_name='Название жанра',
                            help_text='Укажите название жанра')
    slug = models.SlugField(unique=True, verbose_name='Slug жанра',
                            help_text='Задайте уникальный Slug жанра')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=256, db_index=True,
                            verbose_name='Название произведения',
                            help_text='Укажите название произведения')

    year = models.DateField(null=True, blank=True,
                            verbose_name='Год выпуска',
                            help_text='Задайте год выпуска')

    description = models.TextField(null=True, blank=True,
                                   verbose_name='Описание')
    category = models.ForeignKey(Category, verbose_name='Категория',
                                 on_delete=models.SET_NULL,
                                 related_name="titles", blank=True, null=True)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр',
                                   related_name="titles", blank=True)

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name

User = get_user_model()

def ScoreValidator(value):
    if not value >= 0 and value <= 10:
        raise ValidationError('incorrect Score')


class Review(models.Model):
    titles = models.ForeignKey(
        Title, on_delete=models.CASCADE
    )
    score = models.IntegerField(
        verbose_name='Оценка',
        validators=[ScoreValidator],
        default=0,
        blank=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'titles')


class Comment(models.Model):
    titles = models.ForeignKey(
        Title, on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='comments'
    )
    text = models.TextField(
        help_text='Введите текст коментария',
        verbose_name='Текст коментария',
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
