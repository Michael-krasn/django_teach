from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми данными'

    def handle(self, *args, **options):
        # Очистка существующих данных
        self.stdout.write('Очистка существующих данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создание категорий
        self.stdout.write('Создание категорий...')
        electronics = Category.objects.create(
            name='Электроника',
            description='Смартфоны, ноутбуки, планшеты'
        )
        clothing = Category.objects.create(
            name='Одежда',
            description='Мужская и женская одежда'
        )
        books = Category.objects.create(
            name='Книги',
            description='Художественная литература'
        )

        # Создание продуктов
        self.stdout.write('Создание продуктов...')
        Product.objects.create(
            name='Смартфон Xiaomi 13',
            description='8/256GB, AMOLED экран',
            category=electronics,
            price=39990.00
        )
        Product.objects.create(
            name='Ноутбук Apple MacBook Air',
            description='M1, 8/256GB',
            category=electronics,
            price=89990.00
        )
        Product.objects.create(
            name='Джинсы классические',
            description='Синие, прямой крой',
            category=clothing,
            price=3490.00
        )
        Product.objects.create(
            name='Футболка хлопковая',
            description='Белая, размер M',
            category=clothing,
            price=1290.00
        )
        Product.objects.create(
            name='Python. Полное руководство',
            description='Дэвид Бизли',
            category=books,
            price=1890.00
        )

        self.stdout.write(self.style.SUCCESS('✅ База данных успешно заполнена тестовыми данными!'))

        # Вывод статистики
        categories_count = Category.objects.count()
        products_count = Product.objects.count()
        self.stdout.write(f' Создано категорий: {categories_count}')
        self.stdout.write(f' Создано продуктов: {products_count}')
