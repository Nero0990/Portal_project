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

Инструкция по применению миграций в Django:

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

После этого можно начинать создавать миграции. Для этого введите следующую команду в терминале (находясь в директории проекта):

# python3 manage.py makemigrations

Выполните миграцию для создания таблиц базы данных:

# python3 manage.py migrate

Запустите сервер разработки Django:

# python3 manage.py runserver

Создание суперпользователя в Django

Суперпользователь в Django - это пользователь, который имеет все права и привилегии в приложении. Чтобы создать суперпользователя, выполните следующую команду в терминале:

# python3 manage.py createsuperuser

Введите имя пользователя, адрес электронной почты и пароль для суперпользователя.

Примечания

Убедитесь, что у вас установлены все необходимые пакеты и зависимости для работы с базой данных и Django.
Не забудьте указать ENGINE соответствующий написанный вами движок базы данных. В примере выше используется PostgreSQL.
Чтобы ознакомиться со всеми доступными командами `manage.py`, выполните команду `python manage.py help`

Посетить http://127.0.0.1:8000 / в вашем веб-браузере для просмотра главной страницы корпоративного портала. По URL-адресам /instruction и /question будут отображаться сообщения с инструкциями и ответами на часто задаваемые вопросы соответственно.

Используемые библиотеки:
-- Django - Python Web Framework
-- psycopg2-binary - PostgreSQL базы данных для Python# Portal_project
16-05-2023
