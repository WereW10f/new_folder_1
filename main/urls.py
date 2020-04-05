from django.conf.urls import url
from django.urls import URLPattern
from .views import testPage,buildUserPage
urlpatterns=[
    url(r'^$',testPage,name='testPage'),
    url('users/',buildUserPage,name='buildUserPage')

]