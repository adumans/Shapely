from matplotlib import pyplot
from shapely.geometry import LineString ,Polygon
from descartes import PolygonPatch

from figures import SIZE, BLUE, GRAY, RED, set_limits, plot_line

line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])
line1 = LineString([(0,0),(4,4),(8,4),(12,0)])
#line2 = LineString([(0,0),(8,4),(12,4),(12,0)])
pointlist = ((0,0),(8,4),(12,4),(12,0))
line2 = LineString(pointlist)

fig = pyplot.figure(1, figsize=SIZE, dpi=90)

dilated = line.buffer(0.5, cap_style=3)
# 0
ax = fig.add_subplot(221)
plot_line(ax, line1)
plot_line(ax, line2)

dilated1 = line1.buffer(0.9, cap_style=3)
dilated2 = line2.buffer(0.9, cap_style=3)
dilated1 = dilated1.union(dilated2)

patch1 = PolygonPatch(dilated1, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
#patch2 = PolygonPatch(dilated2, fc=BLUE, ec=RED, alpha=0.5, zorder=2)
ax.add_patch(patch1)
#ax.add_patch(patch2)
print('dilated:')
print(dilated)

ax.set_title('a) dilation, cap_style=3')

set_limits(ax, -1, 15, -1, 5)

# 1
'''
ax = fig.add_subplot(121)

plot_line(ax, line)


patch1 = PolygonPatch(dilated, fc=BLUE, ec=RED, alpha=0.5, zorder=2)
ax.add_patch(patch1)
print('dilated:')
print(dilated)

ax.set_title('a) dilation, cap_style=3')

set_limits(ax, -1, 4, -1, 3)
'''
#2
ax = fig.add_subplot(222)

patch2a = PolygonPatch(dilated1, fc=GRAY, ec=GRAY, alpha=0.5, zorder=1)
#ax.add_patch(patch2a)

eroded = dilated1.buffer(-0.1)

# GeoJSON-like data works as well

polygon = eroded.__geo_interface__
# >>> geo['type']
# 'Polygon'
# >>> geo['coordinates'][0][:2]
# ((0.50502525316941682, 0.78786796564403572), (0.5247963548222736, 0.8096820147509064))
patch2b = PolygonPatch(polygon, fc=BLUE, ec=RED, alpha=0.5, zorder=2)
ax.add_patch(patch2b)
print('polygon:')
print(len(polygon['coordinates'][0]))
print(len(polygon['coordinates'][1]))

ax.set_title('b) erosion, join_style=1')

set_limits(ax, -1, 15, -1, 5)

# 3
ax = fig.add_subplot(223)
polygon3 = Polygon(polygon['coordinates'][0])
#polygon3 = Polygon(polygon['coordinates'][0],[polygon['coordinates'][1]])
patch3 = PolygonPatch(polygon3, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax.add_patch(patch3)
ax.set_title('c) erosion[exterior]')
set_limits(ax, -1, 15, -1, 5)

# 4
ax = fig.add_subplot(224)
polygon3 = Polygon(polygon['coordinates'][1])
patch3 = PolygonPatch(polygon3, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax.add_patch(patch3)
ax.set_title('d) erosion[interiors]')
set_limits(ax, -1, 15, -1, 5)

pyplot.show()

