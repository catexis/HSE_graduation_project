from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='index'),

    # Tables
    url(r'^table_cpu/$', views.TableCpu.as_view(), name='table_cpu'),
    url(r'^table_hdd/$', views.TableHDD.as_view(), name='table_hdd'),
    url(r'^table_vga/$', views.TableVGA.as_view(), name='table_vga'),
    url(r'^table_ram/$', views.TableRAM.as_view(), name='table_ram'),
    
    # Compare
    url(r'^create/$', views.ConfCreateView.as_view(), name='conf_create'),

    # url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]