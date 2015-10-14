from netcontrol.network import Network


def get_devices():
    return Network().get_all_connected_devices()
