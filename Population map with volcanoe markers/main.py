import folium
import pandas as pd
data = pd.read_csv("Volcanoes.txt")
print(data)
lat=list(data["LAT"])
lon= list(data["LON"])
elev= list(data["ELEV"])

def colors(el):
    if el < 1000:
        return "green"
    elif 1000<=el<=3000:
        return "orange"
    else:
        return "red"

map=folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fgv= folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=8, popup=str(el)+"m",
                                     fill_color=colors(el),color="grey",fill_opacity=0.8))

fgp= folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
                            style_function=lambda x: {'fillColor':'green' if x["properties"]["POP2005"]<10000000
                            else "orange" if 10000000<=x["properties"]["POP2005"]<=20000000 else "red"}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")