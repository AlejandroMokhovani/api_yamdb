from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils.translation import gettext_lazy as _


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
        'Роль',
        max_length=3,
        choices=ROLE_CHOICES,
        default=USER,
    )
    bio = models.TextField('Биография', blank=True)
