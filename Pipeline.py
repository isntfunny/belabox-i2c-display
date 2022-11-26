from Belabox import getBelaboxConfig, belacoderPipelinesDir
from os import listdir
from os.path import isfile, join
import hashlib


def getPipelines():
    readingPath = belacoderPipelinesDir + '/jetson/'
    pipelines = {}

    for f in listdir(readingPath):
        fullpath = join(readingPath, f)
        if isfile(fullpath):
            encodingStr = 'jetson/' + f
            id = hashlib.sha1(encodingStr.encode('utf-8')).hexdigest()
            pipelines[id] = {'name': f, 'path': fullpath}

    return pipelines


def searchPipelines(indexHash):
    pipelines = getPipelines()
    if indexHash in pipelines:
        return pipelines[indexHash]
    return None


def getPipelineName():
    config = getBelaboxConfig()
    path = searchPipelines(config['pipeline'])

    if path is None:
        return None

    return path['name'].replace('h265_', '').replace('_', ' ')
