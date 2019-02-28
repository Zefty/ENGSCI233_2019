# overpass_ex1.py
# ENGSCI233: Computational Techniques and Computer Systems
# A simple overpass example, for inspecting and exploring the returned data structure.

from overpass import API

api = API()
dat = api.get('node["amenity"="pub"](-36.89,174.70,-36.83,174.80)', responseformat='json')

# set a breakpoint on the line below then run this script in debug mode
print(dat)