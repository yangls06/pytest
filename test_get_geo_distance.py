import math

def get_geo_distance(lng1, lat1, lng2, lat2) -> float:
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

def main():
    center = (121.393967,31.172633)
    pois = [(121.397980,31.170396), (121.399819,31.167021)]
    
    for poi in pois:
        dist = get_geo_distance(center[0], center[1], poi[0], poi[1])
        res = '{} -> {}: {} meters'.format(center, poi, dist)
        print(res)
    

if __name__ == "__main__":
    main()