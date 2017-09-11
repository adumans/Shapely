import os
import time
import json

def loadcarData(path):
    if (os.path.exists(path)):
        files = os.listdir(path)
        for file in files:
            # 得到该文件下所有目录的路径
            subpath = os.path.join(path, file)
            # 判断该路径下是否是文件夹
            if (os.path.isdir(subpath)):
                cartraceblock = {}
                subfiles = os.listdir(subpath)
                for subfile in subfiles:
                    print('in processing %d in %d ' % (subfiles.index(subfile), len(subfiles)))
                    realfile = os.path.join(subpath, subfile)
                    traceblocks = []
                    for line in open(realfile):
                        item = line.split(',')
                        mapblock = pointInwhichsamearea(float(item[4]), float(item[5]))
                        if mapblock:
                            traceblocks.append(mapblock)
                        carnum = item[2]
                    if len(traceblocks):
                        if carnum in cartraceblock:
                            cartraceblock[carnum].append(traceblocks)
                        else:
                            cartraceblock[carnum] = []
                            cartraceblock[carnum].append(traceblocks)

                jsObj = json.dumps(cartraceblock)
                savetype = '.json'
                savename = file + savetype
                fileobject = open(savename, 'w')
                fileobject.write(jsObj)
                fileobject.close()





def loadcarData0():
    cartraceblock = {}
    filepath = '/home/djh/pu/carData/20111107/'
    files = os.listdir(filepath)
    for file in files:
        print('in processing %d in %d ' % (files.index(file), len(files)))
        realfile = os.path.join(filepath, file)
        traceblocks = []
        for line in open(realfile):
            item = line.split(',')
            mapblock = pointInwhichsamearea(float(item[4]), float(item[5]))
            if mapblock:
                traceblocks.append(mapblock)
            carnum = item[2]
        if len(traceblocks):
            if carnum in cartraceblock:
                cartraceblock[carnum].append(traceblocks)
            else:
                cartraceblock[carnum]=[]
                cartraceblock[carnum].append(traceblocks)

    jsObj = json.dumps(cartraceblock)
    fileobject = open('Carblocks.json', 'w')
    fileobject.write(jsObj)
    fileobject.close()


def pointInwhichsamearea(lon, lat):
    MINLON = 116.1713
    MINLAT = 39.7505
    MAXLON = 116.5814
    MAXLAT = 40.0486
    NUMS = 200
    deltlon = (MAXLON - MINLON)/NUMS
    deltlat = (MAXLAT - MINLAT)/NUMS
    if lon < MAXLON and lon > MINLON and lat < MAXLAT and lat > MINLAT:
        x = int((lon - MINLON)/deltlon)
        y = int((lat - MINLAT)/deltlat)
        return (y * NUMS + x)
    else:
        return None


if __name__ == "__main__":
    time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #loadcarData()



    filepath = '/home/djh/pu/carData/'
    loadcarData(filepath)

    # a = pointInwhichsamearea(116.3, 40.0)
    # print (a)
    time2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print (time1)
    print (time2)
    print('done')