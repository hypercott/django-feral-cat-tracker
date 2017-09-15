from django.conf.urls import url

from . import views
from .models import CatColony

urlpatterns = [
    url(r'^$', views.index, name='cattrack-index'),
    url(r'^colonies$', views.colonies, name='cattrack-colonies'),
#    url(r'^colonies/(?P<pk>[0-9]+)/$', views.DetailView.as_view(model=CatColony), name='cattrack-colony-detail'),
#    url(r'^colonies/(?P<pk>[0-9]+)/$', views.ColonyDetail.as_view(), name='cattrack-colony-detail'),
    url(r'^colonies/(?P<pk>[0-9]+)/$', views.colony_detail, name='cattrack-colony-detail'),
#    url(r'^colonies/edit/(?P<pk>[0-9]+)/$', views.ColonyEditView, name='cattrack-colony-edit'),
    url(r'^colonies/edit/(?P<pk>[0-9]+)/$', views.ColonyEditView.as_view(), name='cattrack-colony-edit'),
]

