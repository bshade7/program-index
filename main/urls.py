from django.conf.urls import url, include
from django.views.generic import TemplateView

from main.programs import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^programs/$', views.program_list, name='program_list'),
    url(r'^programs/create/$', views.program_create, name='program_create'),
    url(r'^programs/(?P<pk>\d+)/update/$', views.program_update, name='program_update'),
    url(r'^programs/(?P<pk>\d+)/delete/$', views.program_delete, name='program_delete'),
]
