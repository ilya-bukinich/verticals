from io import StringIO
from django.core.files import File
from django.test import TestCase
from PIL import Image
from django.urls import reverse

from bbs.models import Advert, Category


def test_get_image_file(name='test.png', ext='png', size=(50, 50), color=(256, 0, 0)):
    file_obj = StringIO()
    image = Image.new("RGBA", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)


class AdvertModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(
            id='1',
            name='Test Category'
        )

        Advert.objects.create(
            title='Test Advert',
            summary='Test advert description',
            price=1000,
            author='Bob',
            category_id='1',
            image='test_get_image_file'
        )

    def test_title_field_max_length(self):
        advert = Advert.objects.get(id=1)
        max_length = advert._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_summary_field_max_length(self):
        advert = Advert.objects.get(id=1)
        max_length = advert._meta.get_field('summary').max_length
        self.assertEquals(max_length, 1000)

    def test_image_upload(self):
        advert = Advert.objects.get(id=1)
        self.assertIsNot('image', None)

    def test_get_absolute_url(self):
        advert=Advert.objects.get(id=1)
        self.assertEquals(advert.get_absolute_url(),'/bbs/advert/1')


class AdvertListViewTest(TestCase):
    def setUp(self):
        number_of_adverts = 17
        for advert_num in range(number_of_adverts):
            Advert.objects.create(title='Sell %s' % advert_num, summary='Sell something %s' % advert_num, )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/bbs/adverts/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('adverts'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'bbs/advert_list.html')
