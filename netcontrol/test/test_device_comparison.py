from unittest import TestCase

from netcontrol.network import Device, UNKNOWN


class DeviceComparisonTest(TestCase):
    def test_that_devices_with_same_mac_are_the_same(self):
        mac_address = 'aa:cc:bb:dd:ee:ff'
        device_1 = Device(ip_address='192.168.0.4', mac_address=mac_address)
        device_2 = Device(ip_address='192.168.0.10', mac_address=mac_address)

        self.assertEqual(device_1, device_2)

    def test_that_devices_with_unkown_mac_are_compared_using_ip(self):
        device_1 = Device(ip_address='192.168.1.40', mac_address=UNKNOWN)
        device_2 = Device(ip_address='192.168.1.41', mac_address=UNKNOWN)

        self.assertNotEqual(device_1, device_2)
