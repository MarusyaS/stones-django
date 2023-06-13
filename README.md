# stones-django

Бэкенд на python для портала EP TUR http://sandbox.rssda.su/ep_tur с тюркскими руническими надписями. 

## Установка необходимых библиотек и python 
Находясь в корневой директории склонированного проекта набрать
### `pip install -r requirements.txt`

## Запуск проекта
### `python manage.py runserver' 
Результат будет доступен по адресу: http://127.0.0.1:8000/ 
На странице будут отражены варианты маршрутов для перехода в выдачу данных (stonelib), приложение с подготовленными с помощью библиотеки React (см. https://github.com/MarusyaS/stones-react) статическими файлами (ep_tur) и админку (admin).

## Навигация по коду
Основные элементы проекта:

База данных: db.sqlite3
Настройки сайта: mysite/settings.py
Модели базы данных: stonelib/models.py
Представления данных: stonelib/views.py
Настройка маршрутизации: stonelib/urls.py
