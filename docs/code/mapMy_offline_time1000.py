from osmapi import OsmApi
from matplotlib import pyplot
from shapely.geometry import LineString ,Polygon
from descartes import PolygonPatch
from figures import SIZE, BLUE, GRAY, RED, set_limits, plot_line
import json
MyApi = OsmApi()
map0 = MyApi.Map(116.34384,39.98189,116.34691,39.98352)

#print (type(map0))
#for d in map0:
 #   json.dump(d,open('map_dict', 'w'))

nodesinfo = {}
waylist = []
for item in map0:
    if item['type'] == 'node':
        nid = item['data']['id']
        nid = str(nid)
        nodesinfo[nid] = [item['data']['lat'], item['data']['lon']]
    if item['type'] == 'way':
        oneway = {}
        nodeids =[]
        nodeslocation = []
        oneway['wayid'] = item['data']['id']
        for nodeid in item['data']['nd']:
            nodexy = [0.0,0.0]
            nodeids.append(nodeid)
            #if MyApi.NodeGet(nodeid)['tag']
            strid = str(nodeid)
            nodexy[0] = nodesinfo[strid][0]
            nodexy[1] = nodesinfo[strid][1]
            nodexy = tuple(nodexy)
            nodeslocation.append(nodexy)
        oneway['nodeids'] = nodeids
        nodeslocation = tuple(nodeslocation)
        oneway['nodeslocation'] = nodeslocation
        waylist.append(oneway)

#plot
fig = pyplot.figure(1, figsize=SIZE, dpi=90)
ax = fig.add_subplot(121)
'''
for oneway in waylist:
    points = oneway['nodeslocation']
    line = LineString(points)
    plot_line(ax, line)
'''
oneway = waylist[0]
points = oneway['nodeslocation']
line = LineString(points)
plot_line(ax, line)

# points1 = ((115.2,39.5),(115.6,39.7),(118.8,39.8))
# line = LineString(points1)
# plot_line(ax, line)

set_limits(ax, 39,40,116,117)
pyplot.show()

for d in waylist:
    f= open('map_dict', 'a')
    json.dump(d,f)
    f.write('\n')
f.close()

print (nodesinfo)

