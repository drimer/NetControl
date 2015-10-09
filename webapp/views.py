from json import dumps
import itertools

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from netcontrol.network import get_ifaces, get_connected, DeviceEncoder


def home(request):
    return HttpResponseRedirect(reverse('devices'))


class DevicesView(View):
    def dispatch(self, *args, **kwargs):
        request = args[0]

        if 'application/json' in request.META.get('HTTP_ACCEPT', ''):
            return self.json(*args, **kwargs)
        else:
            return self.get(*args, **kwargs)

    def json(self, *args, **kwargs):
        del args, kwargs

        devices_lists = [get_connected(iface) for iface in get_ifaces()]
        devices = list(itertools.chain(*devices_lists))
        return HttpResponse(dumps(devices, cls=DeviceEncoder), content_type='application/json')

    def get(self, *args, **kwargs):
        del kwargs

        request = args[0]
        return render(request, 'home.html')
