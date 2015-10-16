from contextlib import contextmanager
import ctypes
import fcntl
from json import JSONEncoder
import re
import socket
import subprocess
import struct
from multiprocessing import Manager, Value, Process

from netcontrol.lib import nmap
from netcontrol.util import singleton

UNKNOWN = 'UNKNOWN'


class BroadcastNotFound(Exception):
    pass


class Device(object):
    def __init__(self, ip_address=UNKNOWN, mac_address=UNKNOWN):
        self.ip_address = ip_address
        self.mac_address = mac_address

    def __cmp__(self, other):
        if (self.mac_address, other.mac_address) == (UNKNOWN, UNKNOWN):
            return cmp(self.ip_address, other.ip_address)

        return cmp(self.mac_address, other.mac_address)


class DeviceEncoder(JSONEncoder):
    # pylint:disable=E0202

    def default(self, obj):
        return {
            'ip_address': obj.ip_address,
            'mac_address': obj.mac_address,
        }


@singleton
class Network(object):
    # pylint:disable=W0201,W0212

    @classmethod
    def setup_attributes(cls):
        mt_manager = Manager()
        cls._instance._devices = mt_manager.list()
        cls._instance.scanner_thread = None
        cls._instance._stop_scanning = Value(ctypes.c_bool, True)

    @contextmanager
    def scan_devices(self):
        self.start_scanning_devices()
        yield
        self.stop_scanning_devices()

    def start_scanning_devices(self):
        self._stop_scanning.value = False
        self.scanner_thread = Process(target=self.__do_scan_devices)
        self.scanner_thread.start()

    def stop_scanning_devices(self):
        self._stop_scanning.value = True
        self.scanner_thread.join(timeout=10)

    def __add_device(self, device):
        if device in self._devices:
            self._devices.pop(self._devices.index(device))

        self._devices.append(device)

    def __do_scan_devices(self):
        while not self._stop_scanning.value:
            ifaces = get_ifaces()

            for iface in ifaces:
                if iface == 'lo':
                    continue

                try:
                    broadcast = get_broadcast_dir(iface)
                    address = broadcast.replace('255', '0') + '/%i' % (
                        8 * ((4 - broadcast.count('255')) % 4))
                    scanner = nmap.PortScanner()
                    scanner.scan(hosts=address, arguments='--dns-servers 4.2.2.1 -sP')
                    for ip_addr in scanner.all_hosts():
                        if scanner[ip_addr].state() == 'up':
                            mac_addr = scanner[ip_addr].mac()
                            device = Device(ip_address=ip_addr, mac_address=mac_addr)
                            self.__add_device(device)
                except BroadcastNotFound:
                    continue

    def get_all_connected_devices(self):
        return list(self._devices)


def get_ifaces():
    output = subprocess.check_output('ifconfig -a'.split())
    ifaces = [line.split(' ')[0] for line in output.split('\n')
              if re.match('^[a-zA-Z0-9]', line)]
    return ifaces


def get_broadcast_dir(iface):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        string = socket.inet_ntoa(
            fcntl.ioctl(
                sock.fileno(),
                0x8919,
                struct.pack('128s', iface[:15])
            )[20:24]
        )
    except IOError:
        raise BroadcastNotFound

    return string
