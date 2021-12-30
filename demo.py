import googlemaps


key = open("google.key").readline().replace("\n", "")
gmaps = googlemaps.Client(key=key)
code = gmaps.geocode("37 Merivale Road Harrow")
lat_long = code[0]["geometry"]["location"]
import pdb

pdb.set_trace()

# lat_long = {'lat': 51.57628949999999, 'lng': -0.3500024}
# code[0]['formatted_address']) -> '37 Merivale Rd, Harrow HA1 4BJ, UK'
