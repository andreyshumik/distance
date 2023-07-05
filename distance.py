from math import radians, sin, cos, acos

def calculate (lat1, long1, lat2, long2):
    dist = 6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1 - long2))
    return dist


gomel = {'lat' : radians(52.4345), 'long' : radians(30.9754), 'name' : 'gomel'}
mogilev = {'lat' : radians(53.8991), 'long' : radians(30.3319), 'name' : 'mogilev'}
minsk = {'lat' : radians(53.9045), 'long' : radians(27.5615), 'name' : 'minsk'}
grodno = {'lat' : radians(53.6685), 'long' : radians(23.81364), 'name' : 'grodno'}
brest = {'lat' : radians(52.0976), 'long' : radians(23.7341), 'name' : 'brest'}
vitebsk = {'lat' : radians(55.1904), 'long' : radians(30.2049), 'name' : 'vitebsk'}

#  формула расстояний  6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1 - long2))

distances = {}
cities = [gomel, mogilev, minsk, grodno, brest, vitebsk]

print(len(cities))

for x in range (len(cities)):
    print(cities[x].get('name'))