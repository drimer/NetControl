#!/usr/bin/env python
import subprocess
import os
import sys

PROJECT_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
sys.path.append(PROJECT_DIR)

from scripts.build_setup import setup

PROJECT_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)


def main():
    setup()

    manage_file = os.path.join(PROJECT_DIR, 'manage.py')
    subprocess.check_call(('python', manage_file, 'test'))


if __name__ == '__main__':
    main()
