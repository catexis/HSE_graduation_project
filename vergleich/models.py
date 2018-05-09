from django.core.exceptions import ValidationError
from django.utils.html import format_html
from django.db import models


# RAM table
class ScrapperBenchRam(models.Model):
    name = models.CharField(max_length=1000, blank=True)
    url = models.URLField(max_length=1000, blank=True)
    speed_read = models.IntegerField(blank=True)
    speed_write = models.IntegerField(blank=True)
    latency = models.IntegerField(blank=True)
    in_stock = models.BooleanField(default=False)
    price = models.FloatField(blank=True, default=-1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# CPU table
class ScrapperBenchCPU(models.Model):
    name = models.CharField(max_length=1000, blank=True)
    url = models.URLField(max_length=1000, blank=True)
    score = models.FloatField(blank=True)
    rank = models.IntegerField(blank=True)
    in_stock = models.BooleanField(default=False)
    price = models.FloatField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


# HDD table
class ScrapperBenchHDD(models.Model):
    name = models.CharField(max_length=1000, blank=True)
    url = models.URLField(max_length=1000, blank=True)
    score = models.FloatField(blank=True)
    rank = models.IntegerField(blank=True)
    in_stock = models.BooleanField(default=False)
    price = models.FloatField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


# Video table
class ScrapperBenchVideo(models.Model):
    name = models.CharField(max_length=1000, blank=True)
    url = models.URLField(max_length=1000, blank=True)
    score = models.FloatField(blank=True)
    rank = models.IntegerField(blank=True)
    in_stock = models.BooleanField(default=False)
    price = models.FloatField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ComputerConf(models.Model):
    cpu = models.ForeignKey('ScrapperBenchCPU', on_delete=models.CASCADE, blank = False, null = False, verbose_name = "Цетральный процессор")
    ram = models.ForeignKey('ScrapperBenchRam', on_delete=models.CASCADE, blank = False, null = False, verbose_name = "Оперативная память")
    hdd = models.ForeignKey('ScrapperBenchHDD', on_delete=models.CASCADE, blank = False, null = False, verbose_name = "Жёсткий диск")
    vga = models.ForeignKey('ScrapperBenchVideo', on_delete=models.CASCADE, blank = False, null = False, verbose_name = "Видеоускоритель")

    def __str__(self):
        return "{0}; {1}; {2}; {3}".format(self.cpu, self.ram, self.hdd, self.vga)

    def clean(self):
        if ComputerConf.objects.all().count() > 6:
            # raise ValidationError('Too many records in model')
            raise ValidationError(format_html('<div class="alert alert-warning alert-dismissible fade show" role="alert">Вы можете добавлять не более 7 конфигураций.<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button></div>'))