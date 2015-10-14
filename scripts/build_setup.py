#!/usr/bin/env python

import os
import subprocess

PROJECT_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
DEPS_FILE = os.path.join(PROJECT_DIR, 'pkg-dependencies.txt')
REQS_FILE = os.path.join(PROJECT_DIR, 'requirements.txt')


def setup():
    with open(DEPS_FILE, 'r') as f:
        for package in f:
            subprocess.check_call(('apt-get', 'install', '-y', package))

    with open(REQS_FILE, 'r') as f:
        for requirement in f:
            subprocess.check_call(('pip', 'install', requirement))


if __name__ == '__main__':
    setup()
