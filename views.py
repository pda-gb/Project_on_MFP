"""Реализация контроллеров на фреймворке"""


# PC. отдельные контроллеры на каждую страницу
def index_view(request):
    return '200', 'MAIN'


def products_view(request):
    return '200', 'products view'


def about_view(request):
    return '200', 'about'


def contacts_view(request):
    return '200', 'contact'

# встроено во фреймворке
# def page_404_view(request):
#     return '404', [b'page_404']


# шаблон-копипаста
# def _view(request):
#     return '00',[b'']
