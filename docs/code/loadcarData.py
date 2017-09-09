import os
import time
time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
def traversalDir_FirstDir(path):
    list = []
    if (os.path.exists(path)):
        files = os.listdir(path)
        for file in files:
            # 得到该文件下所有目录的路径
            m = os.path.join(path, file)
            # 判断该路径下是否是文件夹
            if (os.path.isdir(m)):
                h = os.path.split(m)
                print (h[1])
                list.append(h[1])
        print(list)


traversalDir_FirstDir("/home/djh/pu/carData/20111107/")

def loadcarData():
    carData = {}
    filepath = '/home/djh/pu/carData/20111107/'
    files = os.listdir(filepath)
    for file in files:
        realfile = os.path.join(filepath, file)
        for line in open(realfile):
            item = line.split(',')
            gis = (item[4], item[5])
            onepoint = [gis,item[3]]
            if item[2] in carData.keys():
                carData[item[2]].append(onepoint)
            else:
                carData[item[2]] = [onepoint]

    return carData



car = loadcarData()
time2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print (time1)
print (time2)
print('done')