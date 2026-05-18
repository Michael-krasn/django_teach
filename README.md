# Django Shop Project

Учебный проект интернет-магазина на фреймворке Django. Проект настроен в соответствии с современными стандартами разработки: конфигурация переведена на базу данных PostgreSQL, а все чувствительные данные и секретные ключи вынесены в переменные окружения.

## Особенности проекта
* **База данных:** PostgreSQL вместо стандартной SQLite.
* **Безопасность:** Использование `django-environ` для защиты `SECRET_KEY` и доступов к БД.
* **Чистый репозиторий:** Настроена корректная фильтрация мусорных файлов (`__pycache__`, локальных баз данных, настроек IDE) через `.gitignore`.

---

## Требования к окружению

Для запуска проекта вам понадобятся:
* Python 3.10+
* PostgreSQL
* Виртуальное окружение (venv)

---

## Инструкция по локальному развертыванию

### 1. Клонирование репозитория
```bash
git clone [https://github.com/Michael-krasn/django_teach.git](https://github.com/Michael-krasn/django_teach.git)
cd django_teach
git checkout dev
``` 

2. Настройка виртуального окружения
Создайте и активируйте виртуальное окружение, после чего установите зависимости:

Bash
python -m venv venv
# Для Windows (PowerShell):
venv\Scripts\activate
# Для macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt

3. Создание файла конфигурации (.env)
В корневой директории проекта (там, где находится manage.py) создайте файл .env и заполните его своими данными:

Plaintext
DEBUG=True
SECRET_KEY=django-insecure-f=ds7kyc%k-=bu46$0-x*0e-aq6b!ebllf&y4^asrbab5fmn_p

DB_NAME=имя_вашей_базы_данных
DB_USER=имя_пользователя_postgres
DB_PASSWORD=ваш_пароль_от_postgres
DB_HOST=127.0.0.1
DB_PORT=5432

4. Применение миграций и запуск
Перед запуском убедитесь, что в вашем PostgreSQL создана пустая база данных с именем, указанным в файле .env.

Выполните миграции для создания структуры таблиц:

Bash
python manage.py migrate
Запустите локальный сервер разработки:

Bash
python manage.py runserver
Проект будет доступен по адресу: http://127.0.0.1:8000/