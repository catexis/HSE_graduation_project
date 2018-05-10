import django_tables2 as tables
from django.utils.html import format_html

from .models import ScrapperBenchCPU, ScrapperBenchHDD, ScrapperBenchRam, ScrapperBenchVideo


class ColumnBool(tables.Column):
    def render(self, value):
        if value == "True" or value == True:
            return format_html('<i class="menu-icon fa fa-check-square-o">')
        else:
            return format_html('<i class="menu-icon fa fa-square-o">')


class ColumnNoPrice(tables.Column):
    def render(self, value):
        if value == -1:
            return format_html('<i class="menu-icon fa fa-minus">')
        else:
            return value


class ColumnLink(tables.Column):
    def render(self, value, record):
        return format_html('<a href="{}" target="_blank">{}</a>', record.url, value)


class CPUTable(tables.Table):
    name = ColumnLink(verbose_name="Имя")
    score = tables.Column(verbose_name="Индекс производительности")
    rank = tables.Column(verbose_name="Позиция")
    in_stock = ColumnBool(verbose_name="В наличии")
    price = ColumnNoPrice(verbose_name="Цена")

    class Meta:
        model = ScrapperBenchCPU
        fields = ('name', 'score', 'rank', 'in_stock', 'price')
        attrs = {'class': 'table table-striped'}


class HDDTable(tables.Table):
    name = ColumnLink(verbose_name="Имя")
    score = tables.Column(verbose_name="Индекс производительности")
    rank = tables.Column(verbose_name="Позиция")
    in_stock = ColumnBool(verbose_name="В наличии")
    price = ColumnNoPrice(verbose_name="Цена")

    class Meta:
        model = ScrapperBenchHDD
        fields = ('name', 'score', 'rank', 'in_stock', 'price')
        attrs = {'class': 'table table-striped'}


class VGATable(tables.Table):
    name = ColumnLink(verbose_name="Имя")
    score = tables.Column(verbose_name="Индекс производительности")
    rank = tables.Column(verbose_name="Позиция")
    in_stock = ColumnBool(verbose_name="В наличии")
    price = ColumnNoPrice(verbose_name="Цена")

    class Meta:
        model = ScrapperBenchVideo
        fields = ('name', 'score', 'rank', 'in_stock', 'price')
        attrs = {'class': 'table table-striped'}


class RAMTable(tables.Table):
    name = ColumnLink(verbose_name="Имя")
    speed_read = tables.Column(verbose_name="Скорость чтения")
    speed_write = tables.Column(verbose_name="Скорость записи")
    latency = tables.Column(verbose_name="Задержка")
    in_stock = ColumnBool(verbose_name="В наличии")
    price = ColumnNoPrice(verbose_name="Цена")

    class Meta:
        model = ScrapperBenchVideo
        fields = ('name', 'speed_read', 'speed_write', 'latency', 'in_stock', 'price')
        attrs = {'class': 'table table-striped'}
