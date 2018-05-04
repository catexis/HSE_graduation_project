from django.shortcuts import render
from django.views.generic import TemplateView
from . import models
from django.core.paginator import Paginator
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin, SingleTableView
from .tables import CPUTable, HDDTable, VGATable, RAMTable


class IndexPage(TemplateView):
    template_name = "vergleich/index.html"
    flag_main = 'class=active'


class TableCpu(SingleTableView):
    template_name = "vergleich/table_view.html"
    flag_table_cpu = 'class=active'
    queryset = models.ScrapperBenchCPU.objects.all()
    table_class = CPUTable
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TableCpu, self).get_context_data(**kwargs)
        context['page_name'] = "Центральные процессоры"
        return context


class TableHDD(SingleTableView):
    template_name = "vergleich/table_view.html"
    flag_table_hdd = 'class=active'
    queryset = models.ScrapperBenchHDD.objects.all()
    table_class = CPUTable
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TableHDD, self).get_context_data(**kwargs)
        context['page_name'] = "Жёсткие диски"
        return context


class TableVGA(SingleTableView):
    template_name = "vergleich/table_view.html"
    flag_table_vga = 'class=active'
    queryset = models.ScrapperBenchVideo.objects.all()
    table_class = CPUTable
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TableVGA, self).get_context_data(**kwargs)
        context['page_name'] = "Видеоускорители"
        return context


class TableRAM(SingleTableView):
    template_name = "vergleich/table_view.html"
    flag_table_ram = 'class=active'
    queryset = models.ScrapperBenchRam.objects.all()
    table_class = RAMTable
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TableRAM, self).get_context_data(**kwargs)
        context['page_name'] = "Оперативная память"
        return context
