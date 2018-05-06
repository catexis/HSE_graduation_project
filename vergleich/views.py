from . import models
from . import filters
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.core.paginator import Paginator
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin, SingleTableView
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from .tables import CPUTable, HDDTable, VGATable, RAMTable


class IndexPage(TemplateView):
    template_name = "vergleich/index.html"
    flag_main = 'class=active'


class TableCpu(SingleTableMixin, FilterView):
    template_name = "vergleich/table_view.html"
    flag_table_cpu = 'class=active'
    model = models.ScrapperBenchCPU
    queryset = models.ScrapperBenchCPU.objects.all().order_by('-in_stock', '-score')
    table_class = CPUTable
    paginate_by = 10
    filterset_class = filters.TableCPUFilter

    def get_context_data(self, **kwargs):
        context = super(TableCpu, self).get_context_data(**kwargs)
        context['page_name'] = "Центральные процессоры"
        context['filter'] = self.filterset_class
        return context


class TableHDD(SingleTableMixin, FilterView):
    template_name = "vergleich/table_view.html"
    flag_table_hdd = 'class=active'
    queryset = models.ScrapperBenchHDD.objects.all().order_by('-in_stock', '-score')
    table_class = HDDTable
    paginate_by = 10
    filterset_class = filters.TableHDDFilter

    def get_context_data(self, **kwargs):
        context = super(TableHDD, self).get_context_data(**kwargs)
        context['page_name'] = "Жёсткие диски"
        context['filter'] = self.filterset_class
        return context


class TableVGA(SingleTableMixin, FilterView):
    template_name = "vergleich/table_view.html"
    flag_table_vga = 'class=active'
    model = models.ScrapperBenchVideo
    queryset = models.ScrapperBenchVideo.objects.all().order_by('-in_stock', '-score')
    table_class = VGATable
    paginate_by = 10
    filterset_class = filters.TableVGAFilter

    def get_context_data(self, **kwargs):
        context = super(TableVGA, self).get_context_data(**kwargs)
        context['page_name'] = "Видеоускорители"
        context['filter'] = self.filterset_class
        return context


class TableRAM(SingleTableMixin, FilterView):
    template_name = "vergleich/table_view.html"
    flag_table_ram = 'class=active'
    model = models.ScrapperBenchRam
    queryset = models.ScrapperBenchRam.objects.all().order_by('-in_stock', '-speed_read')
    table_class = RAMTable
    paginate_by = 10
    filterset_class = filters.TableRamFilter

    def get_context_data(self, **kwargs):
        context = super(TableRAM, self).get_context_data(**kwargs)
        context['page_name'] = "Оперативная память"
        context['filter'] = self.filterset_class
        return context


class ConfCreateView(FormView):
    pass
