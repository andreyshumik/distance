from math import radians, sin, cos, acos

def calculate (lat1, long1, lat2, long2):
    dist = 6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1 - long2))
    return dist


gomel = {lat : radians(52.4345), long : radians(30.9754)}
mogilev = {lat : radians(53.8991), long : radians(30.3319)}
minsk = {lat : radians(53.9045), long : radians(27.5615)}
grodno = {lat : radians(53.6685), long : radians(23.81364)}
brest = {lat : radians(52.0976), long : radians(23.7341)}
vitebsk = {lat : radians(55.1904), long : radians(30.2049)}

#  формула расстояний  6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1 - long2))

distances = {}
cities = [gomel, mogilev, minsk, grodno, brest, vitebsk]

print(len(cities))

for x in range (len(cities)):

    distances[cities[x]] = x
