from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models


def ScoreValidator(value):
    if not value >= 0 and value <= 10:
        raise ValidationError('incorrect Score')

class User(models.Models):
    pass

class Category(models.Models):
    pass

class Genre(models.Models):
    pass


class Titles(models.Models):
    categories = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
    )
    genres = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
    )
    rating = models.IntegerField(
        verbose_name='Средняя Оценка',
        validators=[ScoreValidator],
        default=0,
        blank=True
    )


class Review(models.Models):
    titles = models.ForeignKey(
        Titles, on_delete=models.CASCADE
    )
    score = models.IntegerField(
        verbose_name='Оценка',
        validators=[ScoreValidator],
        default=0,
        blank=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('User', 'Titles')


class Comment(models.Models):
    titles = models.ForeignKey(
        Titles, on_delete=models.CASCADE
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