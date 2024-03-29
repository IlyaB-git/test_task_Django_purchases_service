# Django purchases service with Stripe



Этот проект создан для изучения взаимодействия веб-фреймвордка __Django__
и платёжной системы __Stripe__. 

В проекте есть такие сущности как ***товар***,
***заказ***, ***валюта***




## Структура исходников

- ```purchases/``` - основное приложение
- ```config/``` - настройки
- ```templates/``` - html шаблоны
- ```manage.py``` - запуск и управление сервером

## URL адреса
- GET ```/``` - старница со всеми товарами и формой для создания заказа
- GET ```/buy/{id}/``` - получение session.id для оплаты товара
- GET ```/buy/order/{id}/``` - получение session.id для оплаты заказа
- GET ```/item/{id}/``` - страница товара с формой оплаты
- POST ```/createorder/``` - создание и оплата заказа

## Настройка базы данных

В репозитории уже есть файл базы данных sqltie3, команды ниже требуются после удаления ```db.sqlite3```

Если вы хотите использовать PostgreSQL, внесите в .env свои настройки.

- ```python3 manage.py makemigrations purchases```
- ```python3 manage.py migrate```

Создание суперпользователя
- ```python3 manage.py createsuperuser```

## Запуск

В файле ```.env``` установите свои SECRET_KEY, STRIPE_SK, STRIPE_PK
И установите DEBUG = False.

Для работы с PostgreSQL установите ```DB_ENGINE=django.db.backends.postgresql_psycopg2```, 
а также соответсвующие параметры DB_NAME, DB_PASSWORD, DB_HOST, DB_PORT


- ```python3 manage.py runserver```

## Запуск через  Docker
- ```sudo docker build -t dj_stripe .```
- ```sudo docker run -p 8000:8000 dj_stripe```
