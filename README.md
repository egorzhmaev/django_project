# Проект Django "sitewomen"

Данный сайт представляет собой учебный проект, созданный с целью изучения фреймворка Django.

- Весь код реализован на фреймворке Django
- Реализовал авторизацию и регистрацию пользователей (с формой восстановления пароля через email)
- Система древовидных комментариев с использованием JavaScript и Ajax
- Взаимодействие с базой осуществлялось с помощью Django ORM
- Redis хранит данные о последнем визите пользователя
- Регистрация с подтверждением через email, а так же форма обратной связи реализована через Celery
- Ежедневная копия базы данных через CeleryBeat
- Django REST Framework - permissions, jwt-токен, пагинация
- Тестирование с unittest
- Весь проект был развернут в Docker контейнерах при помощи Docker Compose

## Пример работы сайта

![pic1](https://github.com/egorzhmaev/django_project/blob/master/pics/2024-03-03_15-49-08.png)

![pic2](https://github.com/egorzhmaev/django_project/blob/master/pics/2024-03-03_15-50-28.png)

![pic6](https://github.com/egorzhmaev/django_project/blob/master/pics/2024-04-09_23-34-24%20(1).png)

![pic3](https://github.com/egorzhmaev/django_project/blob/master/pics/2024-03-03_15-51-32.png)

![pic4](https://github.com/egorzhmaev/django_project/blob/master/pics/2024-03-03_15-52-08.png)

![pic5](https://github.com/egorzhmaev/django_project/blob/master/pics/2024-03-03_15-55-16.png)
