from shapely.geometry import Polygon
from shapely.geometry import Point
from shapely.geometry import MultiPolygon
from matplotlib import pyplot
from shapely.geometry import LineString
from descartes import PolygonPatch
from figures import SIZE, BLUE, GRAY, set_limits, plot_line
poly = Polygon(((0,0),(0,1),(1,1),(1,0)))
poly1 = Polygon(((5,5),(6,5),(6,6),(5,6)))
point = Point(4,4)
bool1 = point.within(poly)
bool2 = poly.contains(point)
a1 = point.buffer(1.3)


fig = pyplot.figure(1, figsize=SIZE, dpi=90)
ax0 = fig.add_subplot(221)
patch1 = PolygonPatch(a1, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
patch11 = PolygonPatch(poly1, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax0.add_patch(patch1)
ax0.add_patch(patch11)
set_limits(ax0, 0, 10, 0, 10)




x,y=7,8
pyplot.plot(x,y, '*')
pyplot.show()

b = MultiPolygon([a1, poly1]).is_valid
print (b)