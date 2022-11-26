from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from time import sleep
from Pipeline import getPipelineName
from Belabox import getSensors, isLive
from Network import getAdapterTraffic

serial = i2c(port=1, address=0x3C)
device = sh1106(serial)
pipeline = ""


def drawText(draw, line, text, x=1):
    yPosition = line * 10 + line
    draw.text((x, yPosition), text, fill="white")


def render_display():
    global pipeline

    with canvas(device) as draw:
        c = 0

        # Getting temperature
        drawText(draw, c, "Temp.: " + getSensors() + "°C")

        # Getting live state
        if isLive() is True:
            drawText(draw, c, 'LIVE', 100)

        # Writing pipelines
        if pipeline is not None:
            c += 1
            drawText(draw, c, pipeline)

        # Getting Adapters and Traffic
        ifaces = getAdapterTraffic()
        for key in ifaces:
            iface = ifaces[key]
            if iface['ip'] and "127.0.0.1" not in iface['ip']:
                drawText(draw, c + 1, "{} {}:".format(iface['name'], iface['total']))
                drawText(draw, c + 2, iface['ip'])
                c += 2

    sleep(1)


if __name__ == '__main__':
    pipeline = getPipelineName()

    while True:
        render_display()
    # getAdapterTraffic()
