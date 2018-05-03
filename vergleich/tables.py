import django_tables2 as tables

from .models import ScrapperBenchCPU, ScrapperBenchHDD, ScrapperBenchRam, ScrapperBenchVideo


class CPUTable(tables.Table):
    name = tables.Column(verbose_name="Имя")
    score = tables.Column(verbose_name="Очки")
    rank = tables.Column(verbose_name="Позиция")
    in_stock = tables.Column(verbose_name="В наличии")
    price = tables.Column(verbose_name="Цена")

    class Meta:
        model = ScrapperBenchCPU
        fields = ('name', 'score', 'rank', 'in_stock', 'price')
        attrs = {'class': 'table table-striped'}


class HDDTable(tables.Table):
    name = tables.Column(verbose_name="Имя")
    score = tables.Column(verbose_name="Очки")
    rank = tables.Column(verbose_name="Позиция")
    in_stock = tables.Column(verbose_name="В наличии")
    price = tables.Column(verbose_name="Цена")

    class Meta:
        model = ScrapperBenchHDD
        fields = ('name', 'score', 'rank', 'in_stock', 'price')
        attrs = {'class': 'table table-striped'}


class VGATable(tables.Table):
    name = tables.Column(verbose_name="Имя")
    score = tables.Column(verbose_name="Очки")
    rank = tables.Column(verbose_name="Позиция")
    in_stock = tables.Column(verbose_name="В наличии")
    price = tables.Column(verbose_name="Цена")

    class Meta:
        model = ScrapperBenchVideo
        fields = ('name', 'score', 'rank', 'in_stock', 'price')
        attrs = {'class': 'table table-striped'}
