from matplotlib import pyplot
from shapely.geometry import LineString ,Polygon
from descartes import PolygonPatch
from figures import SIZE, BLUE, GRAY, RED, GREEN, set_limits, plot_line
import json
from tools import listTotuple

def load(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

if __name__ == "__main__":
    filename0 = 'jsonFileTest0.json'
    filename1 = 'jsonFile.json'
    data0 = load(filename0)
    data1 = load(filename1)
    tuple0 = listTotuple(data1['0'][0])
    tuple1 = listTotuple(data1['1'][0])
    tuple2 = listTotuple(data1['2'][0])
    tuple3 = listTotuple(data1['3'][0])
    tuple9 = listTotuple(data1['0'][3])

    fig = pyplot.figure(1, figsize=SIZE, dpi=150)
    ax = fig.add_subplot(121)

    for i in range (1, len(data1['0'])):
        tuple1 = listTotuple(data1['0'][i])
        polygon1 = Polygon(tuple1)
        patch1 = PolygonPatch(polygon1, fc=RED, ec=RED, alpha=0.5, zorder=2)
        ax.add_patch(patch1)

    # polygon0 = Polygon(tuple0)
    # patch0 = PolygonPatch(polygon0, fc=GRAY, ec=GRAY, alpha=0.5, zorder=2)
    # ax.add_patch(patch0)

    ax.set_title('result')
    set_limits(ax, 116, 119, 39, 42)
    pyplot.show()
   # print (data1['0'])