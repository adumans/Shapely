from matplotlib import pyplot
from shapely.geometry import LineString ,Polygon, Point
from shapely.geometry import MultiPolygon
from descartes import PolygonPatch
from docs.code.figures import SIZE, BLUE, GRAY, RED, GREEN, BLACK, YELLOW, WHITE, set_limits, plot_line
import json
from docs.code.tools import listTotuple

def load(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

def pointInWhichPolygon(point, polygonsList):
    is_find = False
    num =0
    for i in range(1,len(polygonsList)):
        tuple1 = listTotuple(polygonsList[i])
        polygon1 = Polygon(tuple1)
        if point.within(polygon1):
            num =i
            is_find= True
            break
    if is_find:
        return num
    else:
        fatpoint = point.buffer(0.0001)
        for i in range(1, len(polygonsList)):
            tuple1 = listTotuple(polygonsList[i])
            polygon1 = Polygon(tuple1)
            if MultiPolygon([fatpoint, polygon1]).is_valid == False:
                num = i
                is_find = True
                break
        if is_find:
            return num
        else:
            return None




def loadjson():
    filename0 = 'jsonFileTest0.json'
    filename1 = 'jsonFile-joinstyle.json'
    data0 = load(filename0)
    data1 = load(filename1)
    # tuple0 = listTotuple(data1['0'][0])
    # tuple1 = listTotuple(data1['1'][0])
    # tuple2 = listTotuple(data1['2'][0])
    # tuple3 = listTotuple(data1['3'][0])
    # tuple9 = listTotuple(data1['0'][3])

    fig = pyplot.figure(1, figsize=SIZE, dpi=150)
    ax = fig.add_subplot(121)

    holenums = len(data1['0'])
    for i in range (1, int(holenums/3)):
        tuple1 = listTotuple(data1['0'][i])
        polygon1 = Polygon(tuple1)
        patch1 = PolygonPatch(polygon1, fc=RED, ec=WHITE, alpha=0.5, zorder=2)
        ax.add_patch(patch1)
    for i in range (int(holenums/3), int(holenums*2/3)):
        tuple1 = listTotuple(data1['0'][i])
        polygon1 = Polygon(tuple1)
        patch1 = PolygonPatch(polygon1, fc=BLUE, ec=WHITE, alpha=0.5, zorder=2)
        ax.add_patch(patch1)
    for i in range (int(holenums*2/3), holenums):
        tuple1 = listTotuple(data1['0'][i])
        polygon1 = Polygon(tuple1)
        patch1 = PolygonPatch(polygon1, fc=GREEN, ec=WHITE, alpha=0.5, zorder=2)
        ax.add_patch(patch1)

    # for i in range (1, len(data1)):
    #     tuple1 = listTotuple(data1[str(i)])
    #     polygon1 = Polygon(tuple1)
    #     patch1 = PolygonPatch(polygon1, fc=RED, ec=RED, alpha=0.5, zorder=2)
    #     ax.add_patch(patch1)

    ax.set_title('result')
    set_limits(ax, 116, 119, 39, 42)

    ax = fig.add_subplot(122)
    for i in range(1, holenums):
        tuple1 = listTotuple(data1['0'][i])
        #ax.annotate(str(i), xy=tuple1[0], xytext= tuple1[30], arrowprops=dict(facecolor='red', shrink=0.1), )
        polygon1 = Polygon(tuple1)
        x = 116.30754
        y = 39.89570
        #pyplot.plot(x, y, '*')
        point0 = Point(x, y)
        a0 = point0.buffer(0.0001)
        patch1 = PolygonPatch(a0, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
        ax.add_patch(patch1)
        # if point0.within(polygon1):
        #     print (i)
        # if polygon1.contains(point0):
        #     print (i)

        if i%6 ==0:
            patch1 = PolygonPatch(polygon1, fc=BLUE, ec=WHITE, alpha=0.5, zorder=2)
        if i%6 ==1:
            patch1 = PolygonPatch(polygon1, fc=GRAY, ec=WHITE, alpha=0.5, zorder=2)
        if i%6 ==2:
            patch1 = PolygonPatch(polygon1, fc=YELLOW, ec=WHITE, alpha=0.5, zorder=2)
        if i%6 ==3:
            patch1 = PolygonPatch(polygon1, fc=GREEN, ec=WHITE, alpha=0.5, zorder=2)
        if i%6 ==4:
            patch1 = PolygonPatch(polygon1, fc=RED, ec=WHITE, alpha=0.5, zorder=2)
        if i%6 ==5:
            patch1 = PolygonPatch(polygon1, fc=BLACK, ec=WHITE, alpha=0.5, zorder=2)
        ax.add_patch(patch1)

    # for i in range (1, len(data1)):
    #     tuple1 = listTotuple(data1[str(i)])
    #     polygon1 = Polygon(tuple1)
    #     patch1 = PolygonPatch(polygon1, fc=RED, ec=RED, alpha=0.5, zorder=2)
    #     ax.add_patch(patch1)

    ax.set_title('result')
    set_limits(ax, 116, 117, 39, 41)

    pyplot.show()
   # print (data1['0'])
if __name__ == "__main__":
    #loadjson()
    # x = 116.312
    # y = 39.8924
    x = 116.30754
    y = 39.89570
    point0 = Point(x, y)
    filename1 = 'jsonFile-8types-0.0014999.json'
    data1 = load(filename1)
    num = pointInWhichPolygon(point0, data1['0'])
    print (num)

