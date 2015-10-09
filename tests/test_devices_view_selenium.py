import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
import mock
from selenium.webdriver.common.by import By
from selenium.webdriver.phantomjs.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from netcontrol.network import Device

WEBDRIVER_MAX_TIMEOUT = 15

MOCK_DEVICES = [
    Device(ip_address='192.168.0.34', mac_address='AA:DD:EE:FF:BB:CC'),
    Device(ip_address='192.168.0.156', mac_address='AA:EE:DD:FF:AA:CC'),
]


def _get_connected_mock(iface):
    del iface

    return MOCK_DEVICES


def _get_ifaces_mock():
    return ['eth0']


class HomeViewSeleniumTest(StaticLiveServerTestCase):
    @mock.patch('webapp.views.get_connected', _get_connected_mock)
    @mock.patch('webapp.views.get_ifaces', _get_ifaces_mock)
    def test_that_home_view_shows_devices_grid(self):
        url = '%s%s' % (self.live_server_url, reverse('devices'))
        driver = WebDriver()
        driver.get(url)

        waiter = WebDriverWait(driver, WEBDRIVER_MAX_TIMEOUT)
        waiter.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'device')))

        device_grid = driver.find_element_by_id('device-grid')
        devices = device_grid.find_elements_by_class_name('device')
        self.assertEqual(len(MOCK_DEVICES), len(devices))

        for device in MOCK_DEVICES:
            self.assertIn(device.ip_address, device_grid.text)
            self.assertIn(device.mac_address, device_grid.text)
