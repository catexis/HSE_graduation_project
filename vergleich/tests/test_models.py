from django.core.exceptions import ValidationError
from django.test import TestCase

from vergleich.models import (ComputerConf, ScrapperBenchCPU, ScrapperBenchHDD,
                              ScrapperBenchRam, ScrapperBenchVideo)


class CpuModelTest(TestCase):

    """Unit tests for CPU model"""

    def setUp(self):
        ScrapperBenchCPU.objects.create(
            name = "Some name of CPU model for test",
            url = "someCPU.url",
            score = 99999,
            rank = -1,
            in_stock = True,
            price = 999999
        )

    def test_cpu_name_max_length(self):
        pos = ScrapperBenchCPU.objects.get(id=1)
        max_length = pos._meta.get_field('name').max_length
        self.assertEquals(max_length, 1000)

    def test_cpu_url_max_length(self):
        pos = ScrapperBenchCPU.objects.get(id=1)
        max_length = pos._meta.get_field('url').max_length
        self.assertEquals(max_length, 1000)

    def test_cpu_model_str_method(self):
        obj = ScrapperBenchCPU.objects.get(id=1)
        self.assertEqual(str(obj), obj.name)


class HDDModelTest(TestCase):

    """Unit tests for HDD model"""

    def setUp(self):
        ScrapperBenchHDD.objects.create(
            name = "Some name of HDD model for test",
            url = "someHDD.url",
            score = 99999,
            rank = -1,
            in_stock = True,
            price = 999999
        )

    def test_hdd_name_max_length(self):
        pos = ScrapperBenchHDD.objects.get(id=1)
        max_length = pos._meta.get_field('name').max_length
        self.assertEquals(max_length, 1000)

    def test_hdd_url_max_length(self):
        pos = ScrapperBenchHDD.objects.get(id=1)
        max_length = pos._meta.get_field('url').max_length
        self.assertEquals(max_length, 1000)

    def test_hdd_model_str_method(self):
        obj = ScrapperBenchHDD.objects.get(id=1)
        self.assertEqual(str(obj), obj.name)


class VGAModelTest(TestCase):

    """Unit tests for VGA model"""

    def setUp(self):
        ScrapperBenchVideo.objects.create(
            name = "Some name of VGA model for test",
            url = "someVGA.url",
            score = 99999,
            rank = -1,
            in_stock = True,
            price = 999999
        )

    def test_vga_name_max_length(self):
        pos = ScrapperBenchVideo.objects.get(id=1)
        max_length = pos._meta.get_field('name').max_length
        self.assertEquals(max_length, 1000)

    def test_vga_url_max_length(self):
        pos = ScrapperBenchVideo.objects.get(id=1)
        max_length = pos._meta.get_field('url').max_length
        self.assertEquals(max_length, 1000)

    def test_vga_model_str_method(self):
        obj = ScrapperBenchVideo.objects.get(id=1)
        self.assertEqual(str(obj), obj.name)


class RAMModelTest(TestCase):

    """Unit tests for RAM model"""

    def setUp(self):
        ScrapperBenchRam.objects.create(
            name = "Some name of RAM model for test",
            url = "someRAM.url",
            speed_read = 1598,
            speed_write = 8951,
            latency = 2587,
            in_stock = True,
            price = 999999
        )

    def test_ram_name_max_length(self):
        pos = ScrapperBenchRam.objects.get(id=1)
        max_length = pos._meta.get_field('name').max_length
        self.assertEquals(max_length, 1000)

    def test_ram_url_max_length(self):
        pos = ScrapperBenchRam.objects.get(id=1)
        max_length = pos._meta.get_field('url').max_length
        self.assertEquals(max_length, 1000)

    def test_ram_model_str_method(self):
        obj = ScrapperBenchRam.objects.get(id=1)
        self.assertEqual(str(obj), obj.name)


class ComputerConfModelTest(TestCase):

    def setUp(self):
        ScrapperBenchRam.objects.create(
            name = "Some name of RAM model for test",
            url = "someRAM.url",
            speed_read = 1598,
            speed_write = 8951,
            latency = 2587,
            in_stock = True,
            price = 999999
        )
        ScrapperBenchVideo.objects.create(
            name = "Some name of VGA model for test",
            url = "someVGA.url",
            score = 99999,
            rank = -1,
            in_stock = True,
            price = 999999
        )
        ScrapperBenchHDD.objects.create(
            name = "Some name of HDD model for test",
            url = "someHDD.url",
            score = 99999,
            rank = -1,
            in_stock = True,
            price = 999999
        )
        ScrapperBenchCPU.objects.create(
            name = "Some name of CPU model for test",
            url = "someCPU.url",
            score = 99999,
            rank = -1,
            in_stock = True,
            price = 999999
        )
        for i in range(0, 8, 1):
            ComputerConf.objects.create(
                cpu = ScrapperBenchCPU.objects.get(id=1),
                ram = ScrapperBenchRam.objects.get(id=1),
                hdd = ScrapperBenchHDD.objects.get(id=1),
                vga = ScrapperBenchVideo.objects.get(id=1)
            )


    def test_computerconf_model_str_method(self):
        obj = ComputerConf.objects.get(id=1)
        self.assertEqual(str(obj), "{0}; {1}; {2}; {3}".format(obj.cpu, obj.ram, obj.hdd, obj.vga))

    def test_computerconf_model_clean_method(self):
        inst = ComputerConf()
        self.assertRaises(ValidationError, inst.clean)
