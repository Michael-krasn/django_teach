# Интернет-магазин на Django

## Описание проекта
Учебный проект интернет-магазина, разрабатываемый в рамках курса по Django. Проект включает в себя каталог товаров, админ-панель, фикстуры для загрузки данных и кастомные команды для заполнения базы данных.

## Технологии
- **Python** 3.10+
- **Django** 4.2.30
- **SQLite** (разработка) / **PostgreSQL** (продакшн)
- **Bootstrap** 5
- **Poetry** (управление зависимостями)

## Структура проекта
internet_shop/
├── catalog/ # Приложение каталог товаров
│ ├── fixtures/ # Фикстуры для загрузки данных
│ │ ├── categories.json # Категории товаров
│ │ └── products.json # Товары
│ ├── management/ # Кастомные команды
│ │ └── commands/
│ │ └── fill_test_data.py # Заполнение тестовыми данными
│ ├── migrations/ # Миграции базы данных
│ ├── templates/ # HTML шаблоны
│ │ └── catalog/
│ │ ├── home.html # Главная страница
│ │ └── contacts.html # Страница контактов
│ ├── admin.py # Настройка админ-панели
│ ├── models.py # Модели Category и Product
│ ├── urls.py # Маршруты приложения
│ └── views.py # Контроллеры
├── config/ # Конфигурация проекта
│ ├── settings.py # Настройки Django
│ ├── urls.py # Главные маршруты
│ └── wsgi.py
├── static/ # Статические файлы
├── .env # Переменные окружения
├── .gitignore # Исключения для Git
├── README.md # Документация
├── manage.py # Управляющий скрипт Django
├── pyproject.toml # Зависимости (Poetry)
└── requirements.txt # Зависимости (pip)

text

## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone <url-репозитория>
cd internet_shop 
```

### 2. Создание и активация виртуального окружения
Через Poetry (рекомендуется):

bash
poetry shell
poetry install
Через venv:

bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
pip install -r requirements.txt

### 3. Применение миграций
bash
python manage.py makemigrations
python manage.py migrate
### 4. Создание суперпользователя
bash
python manage.py createsuperuser
### 5. Заполнение базы данных тестовыми данными
bash
python manage.py fill_test_data
### 6. Запуск сервера
bash
python manage.py runserver
После запуска сервер будет доступен по адресу: http://127.0.0.1:8000/

### Админ-панель
Доступна по адресу: http://127.0.0.1:8000/admin/

### Настройки админ-панели:
Category: отображение id и name, поиск по name

Product: отображение id, name, price, category; фильтрация по категории; поиск по name и description