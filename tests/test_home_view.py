from django.core.urlresolvers import reverse
from django.test import TestCase

from webapp.views import home

__author__ = 'alberto'


class HomeViewTest(TestCase):
    def test_home_view_redirects_to_devices_view(self):
        response = self.client.get(reverse(home), follow=True)
        self.assertRedirects(response, reverse('devices'))
