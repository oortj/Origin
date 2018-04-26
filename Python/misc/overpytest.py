import overpy
import gpxpy.gpx
import sys

gpxdata = gpxpy.gpx.GPX()

api = overpy.Overpass()

result = api.query("""
area["name"="Groningen"]->.boundaryarea;
(
node(area.boundaryarea)["amenity"~"cafe|pub"];
);
out meta;
""")

for node in result.nodes:
    print("{}, {}, {}".format(node.tags.get("name", "n/a"),node.lat, node.lon))
    wpt = gpxpy.gpx.GPXWaypoint(node.lat, node.lon)
    wpt.name=node.tags.get("name", "n/a")
    gpxdata.waypoints.append(wpt)

print(gpxdata.to_xml())
