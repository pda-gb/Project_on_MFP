from MFP.core import Application

from views import index_view, about_view, products_view, contacts_view

# Routes. соответствие адресу свой контроллер
routes = {
    '/': index_view,
    '/products/': products_view,
    '/about/': about_view,
    '/contacts/': contacts_view,
    # '/page_404/': page_404_view
}


# FC. общие контроллеры на все страницы
def fc_secret_key(request):
    # добавляем данные в запрос
    request['secret_key'] = '123456'


def fc_login(request):
    request['login'] = 'user'


def fc_password(request):
    request['password'] = 'password'


def fc_is_admin(request):
    request['is_admin'] = False


fronts_controllers = [fc_secret_key, fc_login, fc_password, fc_is_admin]
# Создаём объект класса "приложение на MFP" и передаём ему: словарь
# url-контроллер; список фрон
application = Application(routes, fronts_controllers)
