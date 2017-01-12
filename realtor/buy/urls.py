from django.conf.urls import url
from .views import list, detail, create, update, delete, home

app_name = 'buy'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^buy/$', list, name='list'),
    url(r'^buy/create/$', create, name='create'),
    url(r'^buy/(?P<id>\d+)/$', detail, name='detail'),
    url(r'^buy/(?P<id>\d+)/edit/$', update, name='update'),
    url(r'^buy/(?P<id>\d+)/delete/$', delete, name='delete'),
]