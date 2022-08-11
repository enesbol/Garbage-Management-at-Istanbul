import streamlit as st
import geopandas as gpd
import folium
import pandas as pd
import osmnx as ox 
import streamlit as st
from streamlit_folium import st_folium
import folium
from streamlit_folium import st_folium
import folium
from folium import GeoJson

st.set_page_config(layout="wide", page_icon = "🌍",initial_sidebar_state="collapsed")

st.title("Map Visualizations")

st.markdown("At the right top corner of the maps, you can change the background of the maps and add or subtract the layers of the map. All of the maps are dynamic multi-layered maps.")

st.subheader(" ➡️ For editing layers yourself you should close the sidebar at the left if it didn't close automatically.")

st.markdown("Maps are the most appropriate method to show these results.")

df = pd.read_csv("Datas/KMeans/KMeans Labeled.csv")


newlist=['Adalar', 'Arnavutköy', 'Ataşehir', 'Avcılar', 'Bahçelievler', 'Bağcılar', 'Bakırköy', 'Başakşehir', 'Bayrampaşa',
 'Beşiktaş', 'Beykoz', 'Beylikdüzü', 'Beyoğlu', 'Büyükçekmece', 'Çatalca', 'Çekmeköy', 'Esenler', 'Esenyurt', 'Eyüpsultan',
 'Fatih', 'Gaziosmanpaşa', 'Güngören', 'Kadıköy', 'Kağıthane', 'Kartal', 'Küçükçekmece', 'Maltepe', 'Pendik', 'Sancaktepe',
 'Sarıyer', 'Silivri', 'Sultanbeyli', 'Sultangazi', 'Şile', 'Şişli', 'Tuzla', 'Ümraniye', 'Üsküdar', 'Zeytinburnu']

df['İlçe'] = newlist







####CHOROPHLETH MAP####### ##############################################################################################################################

#Create Base Map and Districts on it
geo=r"istanbul-districts.json"
file = open(geo, encoding="utf8")
text = file.read()
 
m1 = folium.Map(width="%100",weight="%100")
 
GeoJson(text).add_to(m1)

#Make Chorophleth Map with Using Values from DF and .json file.
m1 = folium.Map([41.2 ,29],tiles="Cartodb Positron", zoom_start=9,width="%100",height="%100")
folium.Choropleth(
    geo_data=text,
    data=df,
    columns=['İlçe','k_means_pred'],
    fill_color = "YlOrRd",
    fill_opacity=0.9, 
    legend_name='Priority',
    key_on='feature.properties.name'
    ).add_to(m1)

df = pd.read_csv('Datas/Homepage/waste_facility.csv')
gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df.LONGTITUDE, df.LATITUDE))
m = folium.Map(location=[41.2,29],zoom_start=9.4, width="%100",height="%100")
colormap = folium.StepColormap(colors=['green','yellow','orange','blue'] ,#renkler
                            )   

marker_kwds=dict(radius=6,fill=True, draggable=True)

m1 = gdf.explore(m=m1 , column="STATUS", cmap=["blue","green"], name="points",marker_kwds= marker_kwds)

#Layer Control
folium.TileLayer('Stamen Water Color').add_to(m1)
folium.TileLayer('openstreetmap').add_to(m1)
folium.TileLayer('Stamen Terrain').add_to(m1)
folium.TileLayer('Stamen Toner').add_to(m1)
folium.TileLayer('cartodbpositron').add_to(m1)
folium.TileLayer('cartodbdark_matter').add_to(m1)
folium.LayerControl().add_to(m1)   

#For displaying object on streamlit
#st_data1 = st_folium(m,width=1000 ,height=500)

###############################################################################################################################################################


st.title("Locations of waste-facilities")


#seçim yeri ekleyip gerekli heatmapi göstericek

st.markdown("That heatmap represents the locations of waste-facilities in Istanbul.")


#STATUSU BASAN MAP
###############################################################################################################################################################
import pandas as pd 
import geopandas as gpd
import folium
df = pd.read_csv('Datas/Homepage/waste_facility.csv')
gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df.LONGTITUDE, df.LATITUDE))
m = folium.Map(location=[41.2,29],zoom_start=9.4, width="%100",height="%100")
colormap = folium.StepColormap(colors=['green','yellow','orange','red'] ,#renkler
                            )

m = gdf.explore(m=m , column="STATUS", cmap=["red","green"], name="points")
# Add layer control so layers can be switched on / off

folium.TileLayer('Stamen Water Color').add_to(m)
folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('Stamen Terrain').add_to(m)
folium.TileLayer('Stamen Toner').add_to(m)
folium.TileLayer('cartodbpositron').add_to(m)
folium.TileLayer('cartodbdark_matter').add_to(m)
folium.LayerControl().add_to(m)
#Layer Control
st_data = st_folium(m,width=1350, height=600)
###############################################################################################################################################################

st.markdown("This map shows waste facilities according to their status.")





import streamlit.components.v1 as components

#st.components.v1.html("Images/Map/shortest_route_map.html", width=None, height=None, scrolling=False)

st.title("Heatmap")

st.markdown("First Layer: **Garbage Per Capita**")
st.markdown("Second Layer: **Garbage Total**")
st.markdown("Third Layer: **Total Population**")


HtmlFile = open("Images/Map/laye3rheatmapson.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code,height = 600)

st.title("Color Map")

st.markdown("This choropleth is created with Istanbul geojson data and our clusters that were created in KMeans.")
st.markdown("From 0-3 the priority increases.")
st.markdown("The areas colored with red are the most priority ones.")



tab1, tab2 = st.tabs(["📈 Map", "🗃 Code"])


tab1.subheader("Map")
st_data1 = st_folium(m1,width=1350 ,height=700)
 
tab2.subheader("Code")
code ='''
from streamlit_folium import st_folium
import folium
from folium import GeoJson
#Create Base Map and Districts on it
geo=r"istanbul-districts.json"
file = open(geo, encoding="utf8")
text = file.read()
 
m1 = folium.Map(width="%100",weight="%100")
 
GeoJson(text).add_to(m1)

#Make Chorophleth Map with Using Values from DF and .json file.
m1 = folium.Map([41.2 ,29],tiles="Cartodb Positron", zoom_start=9,width="%100",height="%100")
folium.Choropleth(
    geo_data=text,
    data=df,
    columns=['İlçe','k_means_pred'],
    fill_color = "YlOrRd",
    fill_opacity=0.9, 
    legend_name='Priority',
    key_on='feature.properties.name'
    ).add_to(m1)

df = pd.read_csv('waste_facility.csv')
gdf = gpd.GeoDataFrame(df, geometry = gpd.points_from_xy(df.LONGTITUDE, df.LATITUDE))
m = folium.Map(location=[41.2,29],zoom_start=9.4, width="%100",height="%100")
colormap = folium.StepColormap(colors=['green','yellow','orange','blue'] ,#renkler
                            )   

marker_kwds=dict(radius=6,fill=True, draggable=True)

m1 = gdf.explore(m=m1 , column="STATUS", cmap=["blue","green"], name="points",marker_kwds= marker_kwds)

#Layer Control
folium.TileLayer('Stamen Water Color').add_to(m1)
folium.TileLayer('openstreetmap').add_to(m1)
folium.TileLayer('Stamen Terrain').add_to(m1)
folium.TileLayer('Stamen Toner').add_to(m1)
folium.TileLayer('cartodbpositron').add_to(m1)
folium.TileLayer('cartodbdark_matter').add_to(m1)
folium.LayerControl().add_to(m1)   

'''
tab2.code(code, language='python')

st.markdown("Blue circles show available waste facilities. Green circles show waste facilities that are under construction.")
st.markdown("As you can see almost of the facilities have been constructed in 3 and 2 level areas.")
st.markdown("Therefore, it can be said that the model is accurate.")


st.title("Some Routes")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Dolmabahçe Hizmet Birimi Beşiktaş - Şişli Merkez**")
    HtmlFile = open("Images/Map/shortest_route_map.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height = 400)

with col2:
    st.markdown("**Hekimbaşı Katı Atık Aktama İstasyonu - Ümraniye**")
    HtmlFile = open("Images/Map/ümranieshortest.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code,height = 400)

col1, col2 = st.columns(2,gap="small")

with col1:
    st.title("Graph")
    #st.title("How route finder works ?")
    st.markdown("First you decide where your map will be centered.")
    st.markdown("A graph will be created based on your place choice.")
    st.markdown("Then you define your start end locations")
    st.markdown("Algorithm will find the closest node to your start and end origins.")
    st.markdown("Then algorithm will find the shortest path between the two nodes.")
    st.markdown("You may display the route on street level.")
    st.image("Images/Map/KAD-ÜMR OSMNX.png")

with col2:
    code='''
import osmnx as ox
import networkx as nx
ox.config(log_console=True, use_cache=True)

# location where you want to find your route
place     = 'Istanbul'
# find shortest route based on the mode of travel
mode      = 'drive'        # 'drive', 'bike', 'walk'
# find shortest path based on distance or time
optimizer = 'distance'        # 'length','time'

#GRAPH OLUŞTURUYOR.

# create graph from OSM within the boundaries of some 
# geocodable place(s)
graph = ox.graph_from_place(place, network_type = mode)

#Başlangıç Bitiş İçin Node'lar bulur.
orig_node = ox.distance.nearest_nodes(graph, 28.467730,41.148239)
dest_node = ox.distance.nearest_nodes(graph, 28.290184,41.091038)

# EN KISA YOLU BULUR.
shortest_route = nx.shortest_path(graph,
                                  orig_node,
                                  dest_node,
                                  weight=optimizer)
    '''
    st.code(code, language='python')


st.title("Conclusion")

st.markdown(" -> The population of the city keeps increasing and the garbage will be also. ")

st.markdown(" -> Because of that managing garbages will be even more important in the future.")

st.markdown("-> The red colored areas are will be firstly affected areas. We may consider looking for some optimization by using machine learning or other tools when making decisions about where new waste facilities should be constructed.")


st.markdown("-> That was a little demonstration of what would be done with that data. If there will be more data related to that field, I'm sure better inspections and projects can be developed.")


st.markdown("Thanks for listening to me.")

