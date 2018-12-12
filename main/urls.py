from django.conf.urls import url, include
from django.views.generic import TemplateView

from main.programs import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^programs/$', views.book_list, name='program_list'),
    url(r'^programs/create/$', views.book_create, name='program_create'),
    url(r'^programs/(?P<pk>\d+)/update/$', views.book_update, name='program_update'),
    url(r'^programs/(?P<pk>\d+)/delete/$', views.book_delete, name='program_delete'),
]
