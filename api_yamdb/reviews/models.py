from django.db import models

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