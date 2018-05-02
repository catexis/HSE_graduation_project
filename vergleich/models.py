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


# CPU table
class ScrapperBenchHDD(models.Model):
    name = models.CharField(max_length=1000, blank=True)
    url = models.URLField(max_length=1000, blank=True)
    score = models.FloatField(blank=True)
    rank = models.IntegerField(blank=True)
    in_stock = models.BooleanField(default=False)
    price = models.FloatField(blank=True)

    def __str__(self):
        return self.name


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
