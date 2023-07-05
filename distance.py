from math import radians, sin, cos, acos

def calculate (lat1, long1, lat2, long2):
    dist = 6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1 - long2))
    return dist




gomel_lat = radians(52.4345)  # -- Gomel
gomel_long = radians(30.9754)
mogilev_lat = radians(53.8991)  # -- Mogilev
mogilev_long = radians(30.3319)
minsk_lat = radians(53.9045)  # -- Minsk
minsk_long = radians(27.5615)
grodno_lat = radians(53.6685)  # -- Grodno
grodno_long = radians(23.8136)
brest_lat = radians(52.0976)  # -- Brest
brest_long = radians(23.7341)
vitebsk_lat = radians(55.1904)  # -- Vitebsk
vitebsk_long = radians(30.2049)

#  формула расстояний  6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1 - long2))

distances = {}
cities = ['gomel', 'mogilev', 'minsk', 'grodno', 'brest', 'vitebsk']

print(len(cities))

for x in range (len(cities)):
    distances[cities[x]] = x
