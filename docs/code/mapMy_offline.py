from osmapi import OsmApi
from matplotlib import pyplot
from shapely.geometry import LineString ,Polygon
from descartes import PolygonPatch
from figures import SIZE, BLUE, GRAY, RED, set_limits, plot_line
import json
MyApi = OsmApi()
types = ['motorway', 'trunk', 'primary', 'secondary','trunk_link', 'motorway_link', 'primary_link', 'tertiary_link', 'traffic_signals', 'bus_stop']

MINLON0 = 116.1900
MINLAT0 = 39.9837
MAXLON0 = 116.3874
MAXLAT0 = 40.0281
map0 = MyApi.Map(116.3874,39.9837,116.3874,39.9837)


MINLON = 116.1804
MINLAT = 39.7500
MAXLON = 116.5567
MAXLAT = 40.0000

addedlat = 0.0355
MINLON_1 = 116.1804
MAXLON_1 = 116.3905
MINLAT1 = 39.7470
MAXLAT1 = MINLAT1 + addedlat
# left part
for i in range(0, 8):
    MINLAT_1 = round(MINLAT1 + i * addedlat, 4)
    MAXLAT_1 = round(MAXLAT1 + i * addedlat, 4)
    print('start collecting map%d  ...' %(i+1))
    print(MINLON_1, MINLAT_1, MAXLON_1, MAXLAT_1)
    # map1 = MyApi.Map(MINLON_1, MINLAT_1, MAXLON_1, MAXLAT_1)
    # map0.extend(map1)
    if MAXLAT_1 >= MAXLAT:
        MAXLAT = MAXLAT_1
    if MINLAT_1 <= MINLAT:
        MINLAT = MINLAT_1
    if MAXLON_1 >= MAXLON:
        MAXLON = MAXLON_1
    if MINLON_1 <= MINLON:
        MINLON = MINLON_1
#right part
MINLON_2 = 116.3905
MAXLON_2 = 116.5567
MINLAT2 = 39.7470
MAXLAT2 = MINLAT2 + addedlat
for i in range(0, 8):
    MINLAT_2 = round(MINLAT2 + i * addedlat, 4)
    MAXLAT_2 = round(MAXLAT2 + i * addedlat, 4)
    print('start collecting map%d  ...' %(i+1))
    print(MINLON_2, MINLAT_2, MAXLON_2, MAXLAT_2)
    # map2 = MyApi.Map(MINLON_2, MINLAT_2, MAXLON_2, MAXLAT_2)
    # map0.extend(map2)
    if MAXLAT_2 >= MAXLAT:
        MAXLAT = MAXLAT_2
    if MINLAT_2 <= MINLAT:
        MINLAT = MINLAT_2
    if MAXLON_2 >= MAXLON:
        MAXLON = MAXLON_2
    if MINLON_2 <= MINLON:
        MINLON = MINLON_2






# MINLON1 = 116.3874
# MINLAT1 = 39.9837
# MAXLON1 = 116.5615
# MAXLAT1 = 40.0281
#
# MINLON2 = 116.1900
# MINLAT2 = 39.9396
# MAXLON2 = 116.3874
# MAXLAT2 = 39.9837
#
# MINLON3 = 116.3874
# MINLAT3 = 39.9396
# MAXLON3 = 116.5701
# MAXLAT3 = 39.9837
#
# MINLON = min(MINLON0, MINLON1, MINLON2, MINLON3)
# MINLAT = min(MINLAT0, MINLAT1, MINLAT2, MINLAT3)
# MAXLON = max(MAXLON0, MAXLON1, MAXLON2, MAXLON3)
# MAXLAT = max(MAXLAT0, MAXLAT1, MAXLAT2, MAXLAT3)

# MINLON = 116.3666
# MINLAT = 39.9623
# MAXLON = 116.4469
# MAXLAT = 39.9937
# print ('start collecting map0 ...')
# map0 = MyApi.Map(MINLON0, MINLAT0, MAXLON0, MAXLAT0)
# print ('start collecting map1 ...')
# map1 = MyApi.Map(MINLON1, MINLAT1, MAXLON1, MAXLAT1)
# print ('start collecting map2 ...')
# map2 = MyApi.Map(MINLON2, MINLAT2, MAXLON2, MAXLAT2)
# print ('start collecting map3 ...')
# map3 = MyApi.Map(MINLON3, MINLAT3, MAXLON3, MAXLAT3)
#
# print ('merge ...')
# map0.extend(map1)
# map0.extend(map2)
# map0.extend(map3)
#map0 = MyApi.Map(116.34384,39.98189,116.34691,39.98352)
#print (type(map0))
#for d in map0:
 #   json.dump(d,open('map_dict', 'w'))
print ('collecting ends!')
print ('start data processing...')
nodesinfo = {}
waylist = []
nodeselected = []
wayselected = []
for item in map0:
    print ('in processing %d in %d ' %(map0.index(item),len(map0)))
    if item['type'] == 'node':
        nid = item['data']['id']
        nid = str(nid)
        nodesinfo[nid] = [item['data']['lat'], item['data']['lon']]
        if 'highway' in item['data']['tag']:
            if item['data']['tag']['highway'] in types:
                nodeselected.append(str(nid))
                nodeselected.append(item['data']['tag']['highway'])
    if item['type'] == 'way':
        oneway = {}
        nodeids =[]
        nodeslocation = []
        oneway['wayid'] = item['data']['id']
        if 'highway' in item['data']['tag']:
            if item['data']['tag']['highway'] in types:
                wayselected.append(str(oneway['wayid']))
                wayselected.append(item['data']['tag']['highway'])
                for nodeid in item['data']['nd']:
                    strid = str(nodeid)
                    nodexy = [0.0,0.0]
                    #if nodesinfo[strid][0] >= MINLAT and nodesinfo[strid][0] <= MAXLAT and nodesinfo[strid][1] >= MINLON and nodesinfo[strid][1] <= MAXLON:
                    nodeids.append(nodeid)
                    #if MyApi.NodeGet(nodeid)['tag']
                    nodexy[0] = nodesinfo[strid][1]
                    nodexy[1] = nodesinfo[strid][0]
                    nodexy = tuple(nodexy)
                    nodeslocation.append(nodexy)

                    if nodexy[1] >= MAXLAT:
                        MAXLAT = nodexy[1]
                    if nodexy[1] <= MINLAT:
                        MINLAT = nodexy[1]
                    if nodexy[0] >= MAXLON:
                        MAXLON = nodexy[0]
                    if nodexy[0] <= MINLON:
                        MINLON = nodexy[0]

                oneway['nodeids'] = nodeids
                nodeslocation = tuple(nodeslocation)
                oneway['nodeslocation'] = nodeslocation
                waylist.append(oneway)
print ('data processing end!')
#plot
fig = pyplot.figure(1, figsize=SIZE, dpi=150)
ax0 = fig.add_subplot(121)
#dilatedAll = Polygon()

line1 = LineString([(MINLON,MINLAT),(MINLON,MAXLAT)])
dilatedAll = line1.buffer(0.0003, cap_style=3)
plot_line(ax0, line1)
line2 = LineString([(MINLON,MAXLAT),(MAXLON,MAXLAT)])
dilated = line2.buffer(0.0003, cap_style=3)
dilatedAll = dilatedAll.union(dilated)
plot_line(ax0, line2)
line3 = LineString([(MAXLON,MAXLAT),(MAXLON,MINLAT)])
dilated = line3.buffer(0.0003, cap_style=3)
dilatedAll = dilatedAll.union(dilated)
plot_line(ax0, line3)
line4 = LineString([(MINLON,MINLAT),(MAXLON,MINLAT)])
dilated = line4.buffer(0.0003, cap_style=3)
dilatedAll = dilatedAll.union(dilated)
plot_line(ax0, line4)



print ('in processing...')

for oneway in waylist:
    if str(oneway['wayid']) in wayselected:
        points = oneway['nodeslocation']
        line = LineString(points)
        dilated = line.buffer(0.0009, cap_style=3)
        dilatedAll = dilatedAll.union(dilated)
        plot_line(ax0, line)
patch = PolygonPatch(dilatedAll, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
#ax0.add_patch(patch)
print ('dilation done!')

ax1 = fig.add_subplot(122)
eroded = dilatedAll.buffer(-0.00000001)
polygon = eroded.__geo_interface__
patch2 = PolygonPatch(polygon, fc=BLUE, ec=RED, alpha=0.5, zorder=1)
ax1.add_patch(patch2)
print ('eroded done!')
print ('start ploting...')
set_limits(ax1, 116,119,39,42)
pyplot.show()

print ('all done !')
# for d in waylist:
#     f= open('map_dict', 'a')
#     json.dump(d,f)
#     f.write('\n')
# f.close()

# print (nodesinfo)
# print (waylist)
