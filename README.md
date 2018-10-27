# django-project-skeleton
Данный репозиторий содержит готовый, настроенный проект Django, на основе которого можно писать новый проект.

1. Backend
2. Frontend

## Backend

Репозиторий содержит основные настройки Django и библиотек:

- allauth
- ckeditor
- restframework
- djangocleanup
- widget_tweaks
- swagger ui
- sentry
- fabric
- django-pug

Для настроек имеются модули base.py, settings.py, prod.py в пакете djps

Для зависимостей созданы 3 файла requirements: base.txt, test.txt, prod.txt. Эти файлы содержатся в папке requirements.
Используется шаблонизатор PUG вместо HTML.

Для проектов используем Python версии 3


## Frontend

- Для сборки статиков используется gulp. 
- Css заменен на stylus
- Рабочая папка src
- В папке src имеются папки scripts и styles, которые содержат код js и stylus соответственно
- Папка libs в вышеупомянутых папках содержит сторонние библиотеки
- back.js содержит код, связанный с backend частью
- front.js содержит соответственно код для frontend'а
- Для билда статиков используйте команду `gulp`. Все билды помещаются в папку staticfiles


## Развертка проекта
Для первоначальной развертки проекта (установка виртуального окружения, библиотек, и т.д.) запустите `./start.sh`