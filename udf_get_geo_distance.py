import math

from odps.udf import annotate
@annotate("double,double,double,double->double")

class GeoDist(object):
   def evaluate(self, lng1, lat1, lng2, lat2):
       return get_geo_distance(lng1, lat1, lng2, lat2)


def get_geo_distance(lng1, lat1, lng2, lat2):
    """Calculate the distance of two (lng, lat) points.
       See http://developer.baidu.com/map/jsdemo.htm#a6_1 for further understanding.

    Args:
        one point (lng1, lat1)
        another point (lng2, lat2)
    Returns:
        float: the distance of the two (lng, lat) point
    """
    R = 6370996.81 # radius of The Earth

    if (lng1 and lat1 and lng2 and lat2):
        if lng1 == lng2 and lat1 == lat2 :
            distance = 0
        else:
            lat1 = lat1 * math.pi / 180
            lng1 = lng1 * math.pi / 180
            lat2 = lat2 * math.pi / 180
            lng2 = lng2 * math.pi / 180
            # print(a_lng,b_lng,a_lat,b_lat)
            distance = R * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lng2 - lng1))
        return distance
    else: 
        return None