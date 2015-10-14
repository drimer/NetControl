#!/usr/bin/env python
import os
import sys

# pylint:disable=W0403
from netcontrol.network import Network

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webconf.settings")

    from django.core.management import execute_from_command_line

    if 'runserver' in sys.argv:
        with Network().scan_devices():
            execute_from_command_line(sys.argv)
    else:
        execute_from_command_line(sys.argv)
