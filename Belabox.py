import json
import subprocess
import re

belacoderExec = "/usr/bin/belacoder"
belacoderPipelinesDir = "/usr/share/belacoder/pipelines"
thermalPath = '/sys/class/thermal/thermal_zone0/temp'


def getSensors():
    t = open(thermalPath, 'r')
    temperature = int(t.read()) / 1000
    t.close()
    return str(temperature)


def getBelaboxConfig():
    r = open('/opt/belaUI/config.json', 'r')
    config = json.loads(r.read())
    return config


def isLive():
    p = subprocess.Popen("ps -A | grep belacoder", stdout=subprocess.PIPE, shell=True)

    response = p.communicate()
    matches = re.search(r"belacoder", str(response), re.MULTILINE)
    if matches:
        return True
    return False
