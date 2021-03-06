from osmapi import OsmApi
from matplotlib import pyplot
import matplotlib
matplotlib.use('Agg')
from shapely.geometry import LineString ,Polygon
from descartes import PolygonPatch
from figures import SIZE, BLUE, GRAY, RED, set_limits, plot_line
import json
import time
time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
MyApi = OsmApi()

RoadTypes = ['motorway', 'trunk', 'primary','trunk_link', 'motorway_link', 'primary_link', 'secondary', 'secondary_link','traffic_signals', 'bus_stop']
RailTypes = ['rail']
MINLON = 116.4081
MINLAT = 39.8896
MAXLON = 116.4461
MAXLAT = 39.9151
map0 = MyApi.Map(MINLON, MINLAT, MAXLON, MAXLAT)




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
            if item['data']['tag']['highway'] in RoadTypes:
                nodeselected.append(str(nid))
                nodeselected.append(item['data']['tag']['highway'])
    if item['type'] == 'way':
        oneway = {}
        nodeids =[]
        nodeslocation = []
        oneway['wayid'] = item['data']['id']
        if 'highway' in item['data']['tag']:
            if item['data']['tag']['highway'] in RoadTypes:
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
        #if 'railway' in item['data']['tag']:
         #   if item['data']['tag']['railway'] in RailTypes:
          #      wayselected.append(str(oneway['wayid']))
           #     wayselected.append(item['data']['tag']['railway'])
            #    for nodeid in item['data']['nd']:
             #       strid = str(nodeid)
              #      nodexy = [0.0, 0.0]
               #     # if nodesinfo[strid][0] >= MINLAT and nodesinfo[strid][0] <= MAXLAT and nodesinfo[strid][1] >= MINLON and nodesinfo[strid][1] <= MAXLON:
                #    nodeids.append(nodeid)
                 #   # if MyApi.NodeGet(nodeid)['tag']
                  #  nodexy[0] = nodesinfo[strid][1]
                   # nodexy[1] = nodesinfo[strid][0]
                    #nodexy = tuple(nodexy)
                    #nodeslocation.append(nodexy)

                    #if nodexy[1] >= MAXLAT:
                     #   MAXLAT = nodexy[1]
                    #if nodexy[1] <= MINLAT:
                     #   MINLAT = nodexy[1]
                    #if nodexy[0] >= MAXLON:
                     #   MAXLON = nodexy[0]
                    #if nodexy[0] <= MINLON:
                     #   MINLON = nodexy[0]

#                oneway['nodeids'] = nodeids
 #               nodeslocation = tuple(nodeslocation)
  #              oneway['nodeslocation'] = nodeslocation
   #             waylist.append(oneway)

print ('data processing end!')
#plot
fig = pyplot.figure(1, figsize=SIZE, dpi=150)
#1
ax0 = fig.add_subplot(221)
#dilatedAll = Polygon()

epsilon = 0.001
cap_style = 3
join_style = 3
line1 = LineString([(MINLON,MINLAT),(MINLON,MAXLAT)])
dilatedAll = line1.buffer(epsilon, cap_style=cap_style, join_style=join_style)
plot_line(ax0, line1)
line2 = LineString([(MINLON,MAXLAT),(MAXLON,MAXLAT)])
dilated = line2.buffer(epsilon, cap_style=cap_style, join_style=join_style)
dilatedAll = dilatedAll.union(dilated)
plot_line(ax0, line2)
line3 = LineString([(MAXLON,MAXLAT),(MAXLON,MINLAT)])
dilated = line3.buffer(epsilon, cap_style=cap_style, join_style=join_style)
dilatedAll = dilatedAll.union(dilated)
plot_line(ax0, line3)
line4 = LineString([(MINLON,MINLAT),(MAXLON,MINLAT)])
dilated = line4.buffer(epsilon, cap_style=cap_style, join_style=join_style)
dilatedAll = dilatedAll.union(dilated)
plot_line(ax0, line4)



print ('in processing...')

for oneway in waylist:
    if str(oneway['wayid']) in wayselected:
        points = oneway['nodeslocation']
        line = LineString(points)
        dilated = line.buffer(epsilon, cap_style=cap_style, join_style=join_style)
        dilatedAll = dilatedAll.union(dilated)
        plot_line(ax0, line)
patch = PolygonPatch(dilatedAll, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax0.add_patch(patch)
print ('dilation done!')
#2
ax1 = fig.add_subplot(222)
erodedn= -0.0002
eroded = dilatedAll.buffer(erodedn, cap_style=cap_style, join_style=2)
eroded = eroded.buffer(-0.00075, cap_style=cap_style, join_style=1)
# eroded = dilatedAll.buffer(-0.00149)
polygon = eroded.__geo_interface__
patch2 = PolygonPatch(polygon, fc=BLUE, ec=RED, alpha=0.5, zorder=1)
ax1.add_patch(patch2)
ax1.set_title(erodedn)
print ('eroded done!')
print ('start ploting...')

print ('saving as json...')
holedict = {}
for i in range(0, len(polygon['coordinates'])):
    holedict[i] = polygon['coordinates'][i]
jsObj = json.dumps(holedict)
fileobject = open('jsonFileTest0.json', 'w')
fileobject.write(jsObj)
fileobject.close()
print('saving end!')

time2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print (time1)
print (time2)

set_limits(ax1, 116,119,39,42)
#3
# ax2 = fig.add_subplot(223)
# polygon3 = Polygon(polygon['coordinates'][0])
# #polygon3 = Polygon(polygon['coordinates'][0],[polygon['coordinates'][1]])
# patch3 = PolygonPatch(polygon3, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
# ax2.add_patch(patch3)
# ax2.set_title('c) erosion[exterior]')
# set_limits(ax2, 116,119,39,42)
pyplot.show()

print ('all done !')
# for d in waylist:
#     f= open('map_dict', 'a')
#     json.dump(d,f)
#     f.write('\n')
# f.close()

# print (nodesinfo)
# print (waylist)
