# Django purchases service wuth Stripe



Этот проект создан для изучения взаимодействия веб-фреймвордка __Django__
и платёжной системы __Stripe__. 

В проекте есть такие сущности как ***товар***,
***заказ***, ***валюта***, ***скидка***




## Структура исходников

- ```purchases/``` - основное приложение
- ```config/``` - настройки
- ```templates/``` - html шаблоны
- ```manage.py``` - запуск и управление сервером

## Настройка базы данных

В репозитории уже есть файл базы данных, команды ниже требуются после удаления ```db.sqlite3```

- ```python3 manage.py makemigrations purchases```
- ```python3 manage.py migrate```

Создание суперпользователя
- ```python3 manage.py createsuperuser```

## Запуск

- ```python3 manage.py runerver```