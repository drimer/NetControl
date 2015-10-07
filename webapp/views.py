from json import dumps
import os
from django.core.urlresolvers import reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from webconf import settings


def home(request):
    return HttpResponseRedirect(reverse('machines'))


class MachinesView(View):
    def dispatch(self, *args, **kwargs):
        request = args[0]

        if 'application/json' in request.META.get('HTTP_ACCEPT', ''):
            return self.json(*args, **kwargs)
        else:
            return self.get(*args, **kwargs)

    def json(self, *args, **kwargs):
        del args, kwargs

        machines = (
            {'ip_address': '192.168.1.100',
             'mac_address': 'AA:AA:AA:AA:AA:AA'},
            {'ip_address': '192.168.1.101',
             'mac_address': 'BB:BB:BB:BB:BB:BB'},
        )
        return HttpResponse(dumps(machines), content_type='application/json')

    def get(self, *args, **kwargs):
        del kwargs

        request = args[0]
        return render(request, 'home.html')
