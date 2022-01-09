# YaMDb
***
### Описание:

Проект API для YaMDb, который собирает отзывы пользователей на различные произведения.

Произведения подразделяются по жанрам и категориям. К произведению можно оставить отзыв. Отзыв содержит оценку по десятибалльной шкале. На отзыв можно оставить комментарий.

Всю информацию по взаимодейтсвию с проектом можно найти на  [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) при локальном развертывании.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AlejandroMokhovani/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Технологии:

- [Django](https://github.com/django/django) - основной фреймворк
- [Django REST framework](https://github.com/encode/django-rest-framework) - API
### Разработчики:
- [Мохов Александр](https://github.com/AlejandroMokhovani)
- [Затушевский Стас](https://github.com/stas-zatushevskii)
- [Авдеенко Александр](https://github.com/dvaxela)
