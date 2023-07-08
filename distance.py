
from math import radians, sin, cos, acos

def calculate (lat1, long1, lat2, long2):
    dist = 6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(long1 - long2))
    return int(dist)


gomel = {'lat' : radians(52.4345), 'long' : radians(30.9754), 'name' : 'gomel'}
mogilev = {'lat' : radians(53.8991), 'long' : radians(30.3319), 'name' : 'mogilev'}
minsk = {'lat' : radians(53.9045), 'long' : radians(27.5615), 'name' : 'minsk'}
grodno = {'lat' : radians(53.6685), 'long' : radians(23.81364), 'name' : 'grodno'}
brest = {'lat' : radians(52.0976), 'long' : radians(23.7341), 'name' : 'brest'}
vitebsk = {'lat' : radians(55.1904), 'long' : radians(30.2049), 'name' : 'vitebsk'}

distances = {}
cities = [gomel, mogilev, minsk, grodno, brest, vitebsk]


for x in cities:
    distances[x.get('name')] = {}
    for i in cities: 
        distances[x.get('name')][i.get('name')] = calculate(x.get('lat'), x.get('long'), i.get('lat'), i.get('long') )
    print(distances[x.get('name')])
    
    



def print_header(header_data):
  f.write(f'<table><tbody>')
  f.write(f'<tr>')
  f.write(f'<td> ------ </td>')
  for value in list(header_data):
    f.write(f'<td>{value}</td>')
  f.write(f'</tr>')

  print_table(header_data)

  f.write(f'</tbody> </table>')


def print_table(data):
    for value in list(data):
       f.write(f'<tr>')
       f.write(f'<td>{value}</td>')
       for i in data.get(value):
          f.write(f'<td> {data.get(value).get(i)} </td>')            
       f.write(f'</tr>')



f = open('xyz.html','w')
print_header(distances)
f.close()