from . import models
from . import filters
from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView, UpdateView
from django.views.generic import FormView
from django.core.paginator import Paginator
from django_tables2 import MultiTableMixin, RequestConfig, SingleTableMixin, SingleTableView
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView
from django.contrib import messages
from django.urls import reverse_lazy
from .tables import CPUTable, HDDTable, VGATable, RAMTable
from . import forms


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
    template_name = "vergleich/create_view.html"
    form_class = forms.ConfCreateForm
    success_url = "."
    req = {}
    type_of_view = 'FormView'

    def form_valid(self, form):
        self.req["form"] = form
        new_obj = models.ComputerConf(
            cpu = form.cleaned_data['cpu'],
            ram = form.cleaned_data['ram'],
            hdd = form.cleaned_data['hdd'],
            vga = form.cleaned_data['vga']
        )
        new_obj.save()
        print(form)
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        ret = super(ConfCreateView, self).get_context_data(**kwargs)
        if self.req.get("form", None) != None:
            ret["form"] = self.req["form"]
            self.req["form"] = None
        return ret


class ConfCmprView(TemplateView):
    template_name = "vergleich/compare_view.html"

    def get_context_data(self, **kwargs):
        ret = super(ConfCmprView, self).get_context_data(**kwargs)
        ret['table_obj'] = models.ComputerConf.objects.all()
        ret['conf_count'] = range(0, models.ComputerConf.objects.all().count(), 1)
        return ret


class ConfUpdate(UpdateView):
    model = models.ComputerConf
    template_name = "vergleich/create_view.html"
    fields = ['cpu', 'ram', 'vga', 'hdd']
    success_url = reverse_lazy('conf_cmpr')
    type_of_view = 'UpdateView'


class ConfDelete(DeleteView):
    model = models.ComputerConf
    success_url = reverse_lazy('conf_cmpr')
