import fcntl
from json import JSONEncoder
import re
import socket
import subprocess
import struct

from netcontrol.lib import nmap

UNKNOWN = 'UNKNOWN'


class BroadcastNotFound(Exception):
    pass


class Device(object):
    def __init__(self, ip_address=UNKNOWN, mac_address=UNKNOWN):
        self.ip_address = ip_address
        self.mac_address = mac_address


class DeviceEncoder(JSONEncoder):
    def default(self, obj):
        return {
            'ip_address': obj.ip_address,
            'mac_address': obj.mac_address,
        }


def get_ifaces():
    output = subprocess.check_output('ifconfig -a'.split())
    ifaces = [line.split(' ')[0] for line in output.split('\n')
              if re.match('^[a-zA-Z0-9]', line)]
    return ifaces


def get_connected(iface):
    if iface == 'lo':
        return []

    try:
        broadcast = get_broadcast_dir(iface)
        address = broadcast.replace('255', '0') + '/%i' % (
            8 * ((4 - broadcast.count('255')) % 4))
        scanner = nmap.PortScanner()
        scanner.scan(hosts=address, arguments='--dns-servers 4.2.2.1 -sP')
        up_hosts = []
        for host in scanner.all_hosts():
            if scanner[host].state() == 'up':
                up_hosts.append(Device(ip_address=host))
        return up_hosts
    except BroadcastNotFound:
        return []


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
