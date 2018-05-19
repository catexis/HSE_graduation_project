from django.test import TestCase

from vergleich import forms, models


class ConfCmprViewTest(TestCase):
    
    def setUp(self):
        models.ScrapperBenchRam.objects.create(
            name = "RamName",
            url = "someRAM.url",
            speed_read = 1598,
            speed_write = 8951,
            latency = 2587,
            in_stock = True,
            price = 999999
        )
        models.ScrapperBenchVideo.objects.create(
            name = "VgaName",
            url = "someVGA.url",
            score = 99999,
            rank = -1,
            in_stock = True,
            price = 999999
        )
        models.ScrapperBenchHDD.objects.create(
            name = "HddName",
            url = "someHDD.url",
            score = 99999,
            rank = -1,
            in_stock = True,
            price = 999999
        )
        models.ScrapperBenchCPU.objects.create(
            name = "CpuName",
            url = "someCPU.url",
            score = 99999,
            rank = -1,
            in_stock = True,
            price = 999999
        )
        models.ComputerConf.objects.create(
            cpu = models.ScrapperBenchCPU.objects.get(id=1),
            ram = models.ScrapperBenchRam.objects.get(id=1),
            hdd = models.ScrapperBenchHDD.objects.get(id=1),
            vga = models.ScrapperBenchVideo.objects.get(id=1)
        )

    def test_forms(self):
        test_date = models.ComputerConf(
            cpu = models.ScrapperBenchCPU.objects.all().first(),
            ram = models.ScrapperBenchRam.objects.all().first(),
            hdd = models.ScrapperBenchHDD.objects.all().first(),
            vga = models.ScrapperBenchVideo.objects.all().first()
        )
        test_form = forms.ConfCreateForm(instance=test_date)
        form_data = {
            'cpu': models.ScrapperBenchCPU.objects.all().first().id,
            'ram': models.ScrapperBenchRam.objects.all().first().id,
            'hdd': models.ScrapperBenchHDD.objects.all().first().id,
            'vga': models.ScrapperBenchVideo.objects.all().first().id
        }
        test_form = forms.ConfCreateForm(form_data, instance=test_date)
        self.assertTrue(test_form.is_valid())
