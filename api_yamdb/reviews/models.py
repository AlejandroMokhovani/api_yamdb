from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField('email', max_length=254, blank=False)
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]
    role = models.CharField(
        'role',
        max_length=10,
        choices=ROLE_CHOICES,
        default=USER,
    )
    bio = models.TextField('biography', blank=True)
    confirmation_code = models.CharField(max_length=254)

    def __str__(self):
        return self.username

    class Meta:
        constraints = [
            # юзер должен быть уникальным
            models.UniqueConstraint(
                fields=['username',],
                name='unique_username'
            ),
            models.UniqueConstraint(
                fields=['email',],
                name='unique_email'
            ),
            # username юзера не должен быть 'me'
            models.CheckConstraint(
                check=~Q(username__iexact='me'),
                name='cant_given_username'
            ),
        ]
