from . import models
import django_filters


class DRYFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    score = django_filters.RangeFilter()
    rank = django_filters.NumberFilter()
    in_stock = django_filters.BooleanFilter()
    price = django_filters.RangeFilter()


class TableCPUFilter(DRYFilter):

    class Meta:
        model = models.ScrapperBenchCPU
        fields = ['name', 'score', 'rank', 'in_stock', 'price']


class TableHDDFilter(DRYFilter):

    class Meta:
        model = models.ScrapperBenchHDD
        fields = ['name', 'score', 'rank', 'in_stock', 'price']


class TableVGAFilter(DRYFilter):

    class Meta:
        model = models.ScrapperBenchVideo
        fields = ['name', 'score', 'rank', 'in_stock', 'price']


class TableRamFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    speed_read = django_filters.RangeFilter()
    speed_write = django_filters.RangeFilter()
    latency = django_filters.RangeFilter()
    in_stock = django_filters.BooleanFilter()
    price = django_filters.RangeFilter()

    class Meta:
        model = models.ScrapperBenchRam
        fields = ['name', 'speed_read', 'speed_write', 'latency', 'in_stock', 'price']