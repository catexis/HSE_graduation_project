from django.conf.urls import url
from django.urls import register_converter, path, include

from . import views


urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    # Tables
    url(r'^table_cpu/$', views.TableCpu.as_view(), name='table_cpu'),
    url(r'^table_hdd/$', views.TableHDD.as_view(), name='table_hdd'),
    url(r'^table_vga/$', views.TableVGA.as_view(), name='table_vga'),
    url(r'^table_ram/$', views.TableRAM.as_view(), name='table_ram'),
    
    # Compare
    url(r'^create/$', views.ConfCreateView.as_view(), name='conf_create'),
    url(r'^compare/$', views.ConfCmprView.as_view(), name='conf_cmpr'),
    path('compare/<int:pk>/update/', views.ConfUpdate.as_view(), name='conf_update'),
    path('compare/<int:pk>/delete/', views.ConfDelete.as_view(), name='conf_delete'),

    # url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]
