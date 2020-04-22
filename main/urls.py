from django.conf.urls import url
from django.urls import URLPattern
from .views import testPage,buildUserPage,builderCommentPage,builderPosition
urlpatterns=[
    url(r'^$',testPage,name='testPage'),
    url('users/',buildUserPage,name='buildUserPage'),
    url('comment/',builderCommentPage,name='comment'),
    url('positions/',builderPosition,name='positions')

]