from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q


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
