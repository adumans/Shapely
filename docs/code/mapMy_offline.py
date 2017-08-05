from osmapi import OsmApi
from matplotlib import pyplot
from shapely.geometry import LineString ,Polygon
from descartes import PolygonPatch
from figures import SIZE, BLUE, GRAY, RED, set_limits, plot_line
import json
MyApi = OsmApi()
types = ['motorway', 'trunk', 'primary', 'secondary', 'trunk_link', 'motorway_link', 'primary_link', 'tertiary_link', 'traffic_signals', 'bus_stop']
print ('start collecting map ...')

MINLON = 116.2992
MINLAT = 39.9005
MAXLON = 116.3555
MAXLAT = 39.9445

# MINLON = 116.3666
# MINLAT = 39.9623
# MAXLON = 116.4469
# MAXLAT = 39.9937

map0 = MyApi.Map(MINLON, MINLAT, MAXLON, MAXLAT)
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
