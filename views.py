"""Реализация контроллеров на фреймворке"""
from MFP.templator import render


# PC. отдельные контроллеры на каждую страницу
def index_view(request):
    data = {
        'title': 'главная',
        'secret_key': request.get('secret_key')
    }
    page = render('index.jinja2', **data)
    return '200', page


def products_view(request):
    data = {
        'title': 'продукты',
        'secret_key': request.get('secret_key')
    }
    page = render('index.jinja2', **data)
    return '200', page


def about_view(request):
    data = {
        'title': 'о нас',
        'secret_key': request.get('secret_key')
    }
    page = render('index.jinja2', **data)
    return '200', page


def contacts_view(request):
    data = {
        'title': 'контакты',
        'secret_key': request.get('secret_key')
    }
    page = render('index.jinja2', **data)
    return '200', page


# шаблон-копипаста
# def _view(request):
#     return '00',[b'']
