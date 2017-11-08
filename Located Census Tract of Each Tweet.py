import json
import gzip
import urllib
import xml.etree.ElementTree as ET
from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    uh = urllib.urlopen(url)
    data = uh.read()
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    center_lat = lat
    center_lng = lng
    print 'lat',lat,'lng',lng
    print 'center_lat',center_lat,'center_lng',center_lng
    print location
    center_lat = float(center_lat)
    center_lng = float(center_lng)

while True:
    Question = raw_input('Do you want to insert the coordination (y/n)?')
    if Question == 'n' : break
    center_lat = float(raw_input('Enter Latitude of Center: '))
    center_lng = float(raw_input('Enter Longitude of Cneter: '))

lat1 = radians(center_lat)
lon1 = radians(center_lng)

# Variabe for Census Tracts within considered ceneter
Radius = float(raw_input('Please enter the cutoff radius (km):   '))



Census = []
Located_Census_Tracts = []

i = 0

PIK = "Census_Tracts" + ".json" + ".gz"
with gzip.open(PIK, "rb") as ff:
    for line in ff:
        Distance_census = []
        Census = json.loads(line)
        for Edge in Census[1]:
            lat2 = radians(Edge[1])
            lon2 = radians(Edge[0])
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = R * c
            Distance_census.append(distance)
        if max(Distance_census) < Radius:
            Located_Census_Tracts.append(Census)

print "Nember of located Census Tracts:  ",len(Located_Census_Tracts)
print Located_Census_Tracts[0]

PIK = "Located_Census_Tracts" + ".json" + ".gz"
with gzip.open(PIK, "wb") as ff:
    for Tract in Located_Census_Tracts:
        json.dump(Tract, ff)
        ff.write('\r\n')
ff.close()


