from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='cattrack-index'),
    url(r'^/colonies$', views.colonies, name='cattrack-colonies'),
]

