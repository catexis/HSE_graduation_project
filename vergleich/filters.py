from . import models
import django_filters


class TableCPUFilter(django_filters.FilterSet):

    class Meta:
        model = models.ScrapperBenchCPU
        fields = {
            'name': ['contains'],
            'score': ['contains'],
            'rank': ['exact'],
            'in_stock': ['exact'],
            'price': ['contains']
        }


class TableHDDFilter(django_filters.FilterSet):

    class Meta:
        model = models.ScrapperBenchHDD
        fields = {
            'name': ['contains'],
            'score': ['contains'],
            'rank': ['exact'],
            'in_stock': ['exact'],
            'price': ['contains']
        }


class TableVGAFilter(django_filters.FilterSet):

    class Meta:
        model = models.ScrapperBenchVideo
        fields = {
            'name': ['contains'],
            'score': ['contains'],
            'rank': ['exact'],
            'in_stock': ['exact'],
            'price': ['contains']
        }


class TableRamFilter(django_filters.FilterSet):

    class Meta:
        model = models.ScrapperBenchRam
        fields = {
            'name': ['contains'],
            'speed_read': ['contains'],
            'speed_write': ['contains'],
            'latency': ['contains'],
            'in_stock': ['exact'],
            'price': ['contains']
        }