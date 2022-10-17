import os


def CheckFile():
    statsPath = getStatsPath()
    return  os.path.isfile(statsPath)

def getStatsPath():
    return os.sep.join([os.getcwd(), "Statistics.txt"])