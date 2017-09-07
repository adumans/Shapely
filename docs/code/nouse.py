from shapely.geometry import Polygon
from shapely.geometry import Point
import matplotlib.pyplot as plt
poly = Polygon(((0,0),(0,1),(1,1),(1,0)))
point = Point(0.001,0.1)
bool1 = point.within(poly)
bool2 = poly.contains(point)

x,y=7,8
plt.plot(x,y, '*')
plt.show()

print (bool1)
print (bool2)