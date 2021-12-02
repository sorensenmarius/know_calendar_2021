import math

def distance(origin, destination):
    lon1, lat1 = origin
    lon2, lat2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d

coords = []
f = open('cities.csv', 'r', encoding="utf8")
for line in f.readlines()[1:]:
    coord = line.strip().split(',')[-1]
    coord = coord.replace('Point(', '')[:-1]
    split = coord.split(' ')
    coords.append((float(split[0]), float(split[1])))

current = (0, 90)
sum = 0
while len(coords) > 0:
    closest = (None, None)
    for coord in coords:
        dist = distance(current, coord)
        if closest[1] is None or dist < closest[1]:
            closest = (coord, dist)
    sum += closest[1]
    coords.remove(closest[0])
    current = closest[1]

sum += distance(current, (0, 90))

print(sum)