Корпоративный портал

Это веб-приложение Django для корпоративного портала, которое содержит инструкции и ответы на часто задаваемые вопросы.

Как запустить этот проект на новом компьютере:
Клонируйте этот репозиторий:
Копировать код
# git clone https://github.com/Nero0990/Portal_project.git

Измените каталог на папку проекта:
# cd corporate-portal

Создайте виртуальную среду и активируйте ее:
# virtualenv venv
# source venv/bin/activate

Установите необходимые библиотеки из `requirements.txt ` файл:
# pip install -r requirements.txt

Настройте свою базу данных PostgreSQL, обновив параметр `DATABASES` в `portal/settings.py `. Замените значения `ИМЯ`, `ПОЛЬЗОВАТЕЛЬ`, `ПАРОЛЬ` вашими собственными учетными данными базы данных в таком формате:
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

Выполните миграцию для создания таблиц базы данных:
# python3 manage.py migrate

Запустите сервер разработки Django:
# python3 manage.py runserver

Посетить http://127.0.0.1:8000 / в вашем веб-браузере для просмотра главной страницы корпоративного портала. По URL-адресам /instruction и /question будут отображаться сообщения с инструкциями и ответами на часто задаваемые вопросы соответственно.

Используемые библиотеки:
-- Django - Python Web Framework
-- psycopg2-binary - PostgreSQL базы данных для Python# Portal_project
