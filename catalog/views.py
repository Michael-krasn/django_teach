from django.shortcuts import render

def home(request):
    """Контроллер для домашней страницы"""
    context = {
        'title': 'Главная страница',
        'page_name': 'Домашняя страница',
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    """Контроллер для страницы с контактной информацией"""
    context = {
        'title': 'Контакты',
        'page_name': 'Свяжитесь с нами',
        'email': 'shop@example.com',
        'phone': '+7 (999) 123-45-67',
        'address': 'г. Москва, ул. Примерная, д. 123',
    }
    return render(request, 'catalog/contacts.html', context)\
