from django.test import TestCase

# Create your tests here.

from vergleich.models import ScrapperBenchCPU

class CpuModelTest(TestCase):

    # @classmethod
    # def setUpTestData(cls):
    def setUp(self):
        ScrapperBenchCPU.objects.create(
            name = "Intel Core i9-7980XE @ Test",
            url = "ya.ru",
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

    def test_cpu_score_type(self):
        pos = ScrapperBenchCPU.objects.get(id=1)
        score = pos.score
        self.assertIsInstance(score, float)
