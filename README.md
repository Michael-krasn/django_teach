```markdown
# Django Интернет-магазин

Веб-приложение интернет-магазина на Django с использованием Bootstrap.

## Структура проекта

```

django_shop/
├── manage.py              # Утилита управления Django
├── requirements.txt       # Зависимости проекта
├── db.sqlite3            # База данных SQLite
├── shop/                 # Основная конфигурация проекта
│   ├── settings.py       # Настройки Django
│   ├── urls.py          # Корневые маршруты
│   └── wsgi.py          # WSGI конфигурация
└── catalog/              # Приложение каталога
├── views.py          # Контроллеры
├── urls.py           # Маршруты приложения
└── templates/        # HTML шаблоны
└── catalog/
├── home.html    # Главная страница
└── contacts.html # Страница контактов

```

## Требования

- Python 3.8+
- Django 4.2+

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd django_shop
```

2. Создание виртуального окружения

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Установка зависимостей

```bash
pip install -r requirements.txt
```

4. Применение миграций

```bash
python manage.py migrate
```

5. Запуск сервера разработки

```bash
python manage.py runserver
```

6. Открытие в браузере

```
http://127.0.0.1:8000/
```

Доступные страницы

URL Описание
/ Главная страница с товарами
/contacts/ Страница контактов с формой

Используемые технологии

· Django 4.2 - веб-фреймворк
· Bootstrap 5 - CSS фреймворк
· SQLite - база данных

Функциональность

· Главная страница с карточками товаров
· Страница контактов с формой обратной связи
· Адаптивный дизайн на Bootstrap
· Навигационное меню между страницами
