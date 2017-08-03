from osmapi import OsmApi
import json
MyApi = OsmApi()
map0 = MyApi.Map(116.34384,39.98189,116.34691,39.98352)

#print (type(map0))
#for d in map0:
 #   json.dump(d,open('map_dict', 'w'))

nodelist = []
waylist = []
for item in map0:
    if item['type'] == 'node':
        nodelist.append(item['data']['id'])
    if item['type'] == 'way':
        oneway = {}
        nodeids =[]
        nodeslocation = []
        oneway['wayid'] = item['data']['id']
        for nodeid in item['data']['nd']:
            nodexy = [0.0,0.0]
            nodeids.append(nodeid)
            #if MyApi.NodeGet(nodeid)['tag']
            d = MyApi.NodeGet(nodeid)
            nodexy[0] = d['lat']
            nodexy[1] = d['lon']
            nodexy = tuple(nodexy)
            nodeslocation.append(nodexy)
        oneway['nodeids'] = nodeids
        nodeslocation = tuple(nodeslocation)
        oneway['nodeslocation'] = nodeslocation
        waylist.append(oneway)







print (nodelist)
print (waylist)
