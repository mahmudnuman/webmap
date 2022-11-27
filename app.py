import folium
import pandas as pd

data=pd.read_csv("Volcanoes.txt")

lattitude=data["LAT"]
longitude=data["LON"]
information= "Name:" + data["NAME"].astype(str) + "\nLocation:"+data["LOCATION"].astype(str) +"\nStatus:" + data["STATUS"].astype(str) + "\nType:" +data["TYPE"].astype(str) + "\nElevation:" + data["ELEV"].astype(str) + ' m'
elevetion=data["ELEV"]

def color_producer(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev <3000:
        return "orange"
    elif 3000 <= elev <5000:
        return "pink"
    else:
        return "red"
        
    

map=folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="OpenStreetMap")

fgv=folium.FeatureGroup(name="Volcanos in USA")
fgp=folium.FeatureGroup(name="Population")


for lat,lon,info,ele in zip(lattitude,longitude,information,elevetion):
    

    fgv.add_child(folium.CircleMarker(location=[lat,lon],
                            radius=7,
                            popup=str(info),
                            fill_color=color_producer(ele), color ="gray",
                            fill_opacity=0.7))


fgp.add_child(folium.GeoJson(data=open('world.json','r',
                                    encoding='utf-8-sig').read(),
                                   style_function=lambda x:{
                                                        'fillColor':'green'
                                                         if x['properties']['POP2005'] <10000000 
                                                         else "orange"
                                                         if 100000000<= x['properties']['POP2005'] <200000000 
                                                         else "red"
                                                            }
                                       ))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map1.html");