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
