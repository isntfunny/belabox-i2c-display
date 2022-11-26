import psutil
from netifaces import AF_INET
import netifaces as ni
import math

io = psutil.net_io_counters(pernic=True)


def get_ip_address(ifname):
    iface = ni.ifaddresses(ifname)
    if iface is not None and AF_INET in iface:
        return iface[AF_INET][0]['addr']

    return ""


def get_size(bitrate):
    return str(math.ceil(bitrate / 1024 * 8)).rjust(4, '0') + " kbps"


def getAdapterTraffic():
    global io
    io_2 = psutil.net_io_counters(pernic=True)

    data = {}
    for iface, iface_io in io.items():
        upload_speed = io_2[iface].bytes_sent - iface_io.bytes_sent
        download_speed = io_2[iface].bytes_recv - iface_io.bytes_recv
        data[iface] = {
            "name": iface,
            "ip": get_ip_address(iface),
            "tx": f"{get_size(upload_speed)}",
            "rx": f"{get_size(download_speed)}",
            "total": f"{get_size(upload_speed + download_speed)}",
        }

    io = io_2
    return data
