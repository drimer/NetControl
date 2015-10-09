from bs4 import BeautifulSoup
from django.core.urlresolvers import reverse
from django.test import TestCase

from webapp.views import home

__author__ = 'alberto'


class HomeViewTest(TestCase):
    def test_home_view_renders_correctly(self):
        response = self.client.get(reverse(home), follow=True)
        self.assertEqual(200, response.status_code)

    def test_home_view_uses_correct_snippets(self):
        response = self.client.get(reverse(home), follow=True)
        self.assertTemplateUsed(response, 'snippets/header.html')

    def test_home_view_shows_loading_message_initially(self):
        response = self.client.get(reverse(home), follow=True)

        bs = BeautifulSoup(response.content)
        device_grid = bs.find(attrs={'id': 'device-grid'})
        loading_text_elems = device_grid.find_all(attrs={'class': 'loading-text'})

        self.assertEqual(1, len(loading_text_elems))
