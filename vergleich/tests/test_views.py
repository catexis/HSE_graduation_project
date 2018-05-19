from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from test_plus.test import CBVTestCase
from vergleich import filters, forms, models
from vergleich.views import (ConfCmprView, ConfCreateView, TableCpu, TableHDD,
                             TableRAM, TableVGA)


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_authenticated)


class TableCpuTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_tablecpu_view_responce(self):
        self.client.login(username='temporary', password='temporary')
        resp = self.client.get(reverse('table_cpu'), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_tablecpu_view_page_context(self):
        self.client.login(username='temporary', password='temporary')
        resp = self.client.get(reverse('table_cpu'), follow=True)
        self.assertEqual(resp.context['page_name'], "Центральные процессоры")
        self.assertEqual(resp.context['filter'], filters.TableCPUFilter)


class TableHDDTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_tablehdd_view_responce(self):
        self.client.login(username='temporary', password='temporary')
        resp = self.client.get(reverse('table_hdd'), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_tablehdd_view_page_context(self):
        self.client.login(username='temporary', password='temporary')
        resp = self.client.get(reverse('table_hdd'), follow=True)
        self.assertEqual(resp.context['page_name'], "Жёсткие диски")
        self.assertEqual(resp.context['filter'], filters.TableHDDFilter)


class TableVGATest(TestCase):

    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_tablevga_view_responce(self):
        self.client.login(username='temporary', password='temporary')
        resp = self.client.get(reverse('table_vga'), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_tablevga_view_page_context(self):
        self.client.login(username='temporary', password='temporary')
        resp = self.client.get(reverse('table_vga'), follow=True)
        self.assertEqual(resp.context['page_name'], "Видеоускорители")
        self.assertEqual(resp.context['filter'], filters.TableVGAFilter)


class TableRAMTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_tablevga_view_responce(self):
        self.client.login(username='temporary', password='temporary')
        resp = self.client.get(reverse('table_ram'), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_tablevga_view_page_context(self):
        self.client.login(username='temporary', password='temporary')
        resp = self.client.get(reverse('table_ram'), follow=True)
        self.assertEqual(resp.context['page_name'], "Оперативная память")
        self.assertEqual(resp.context['filter'], filters.TableRamFilter)


class ConfCmprViewTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
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

    def test_confcmpr_view_responce(self):
        self.client.login(username='temporary', password='temporary')
        resp = self.client.get(reverse('conf_cmpr'), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_confcmpr_view_page_context(self):
        self.client.login(username='temporary', password='temporary')
        resp = self.client.get(reverse('conf_cmpr'), follow=True)
        self.assertEqual(
            range(0, models.ComputerConf.objects.all().count(), 1),
            resp.context['conf_count']
        )


class ConfCreateViewTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
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


    def test_confcmpr_view_page_form(self):
        self.client.login(username='temporary', password='temporary')
        resp = self.client.get(reverse('conf_create'), follow=True)
        test_date = models.ComputerConf(
            cpu = models.ScrapperBenchCPU.objects.all().first(),
            ram = models.ScrapperBenchRam.objects.all().first(),
            hdd = models.ScrapperBenchHDD.objects.all().first(),
            vga = models.ScrapperBenchVideo.objects.all().first(),
        )
        # test_form = forms.ConfCreateForm(instance=test_date)
        test_form = forms.ConfCreateForm()
        self.assertEqual(type(resp.context["form"]), type(test_form))