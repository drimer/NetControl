from bs4 import BeautifulSoup
from django.core.urlresolvers import reverse
from django.test import TestCase

__author__ = 'alberto'


class DevicesViewTest(TestCase):
    def test_devices_view_renders_correctly(self):
        response = self.client.get(reverse('devices'))
        self.assertEqual(200, response.status_code)

    def test_devices_view_uses_correct_snippets(self):
        response = self.client.get(reverse('devices'))
        self.assertTemplateUsed(response, 'snippets/header.html')

    def test_devices_view_shows_loading_message_initially(self):
        response = self.client.get(reverse('devices'))

        bs = BeautifulSoup(response.content)
        device_grid = bs.find(attrs={'id': 'device-grid'})
        loading_text_elems = device_grid.find_all(attrs={'class': 'loading-text'})

        self.assertEqual(1, len(loading_text_elems))
