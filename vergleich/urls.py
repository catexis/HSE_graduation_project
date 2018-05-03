from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name='index'),

    # Tables
    url(r'^table_cpu/$', views.TableCpu.as_view(), name='table_cpu'),
    url(r'^table_hdd/$', views.TableHDD.as_view(), name='table_hdd'),
    url(r'^table_vga/$', views.TableVGA.as_view(), name='table_vga'),
    # url(r'^books/$', views.BookListView.as_view(), name='books'),
    # url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]