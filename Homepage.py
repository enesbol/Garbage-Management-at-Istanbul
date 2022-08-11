import streamlit as st
import pandas as pd
import plotly.express as px
import json 



#read the data

#PATHS WİLL CHANGE TO THE SAME FOLDER DATAS -> REGRESSION 
                                            #-> MAİN FİLE 

df = pd.read_excel("Datas\Homepage\ilce-yl-baznda-evsel-atk-miktar (2).xlsx",engine="openpyxl")
df2 = pd.read_csv("Datas\Homepage\waste_facility.csv")
df3 = pd.read_csv("Datas\Homepage\ilcekonum.csv")





#jdf = geemap.geojson_to_df('istanbul-districts.json')
 
st.title("Abstract")

st.markdown('<span style="font-family:Century Gothi; font-size:1.5em;">We know that important environmental problems can arise in **Metropols** like Istanbul due to population and many other factors. Pollution and **garbage management** are one of them. **Managing**, **recycling** and using optimally to **producing energy** from that garbage must be inside their visions of the cities like that. </span>', unsafe_allow_html=True)

st.markdown('<span style="font-family:Papyrus; font-size:1.5em;">I decided to determine the new waste facilities where should be constructed. For that, we need data about garbage mass, the population of the people that live in every district of the city, locations of the districts, locations of the waste facilities etc. </span>', unsafe_allow_html=True)



st.title("Data Sources")
st.markdown("Data was collected from Istanbul Data Portal and open sources like Github.")

st.title("1-Datas From Istanbul Data Portal")

st.markdown("**1.1- Garbage mass according to districts**")
st.markdown("This data shows the amount of garbage on a per ton basis by districts between 2004 and 2021.")
st.dataframe(df,700,200)

st.markdown("**1.2- Locations of the waste facilities**")
st.markdown("This data shows the Latitude and longitude of garbage facilities.")
st.dataframe(df2,700,200)


st.title("2-Datas From Open Sources")

st.markdown(" **2.1 - Locations of all district centers in Turkey** ")
st.markdown("This data shows the Latitude and longitude of all district centers in Turkey.")
st.dataframe(df3,700,150)


st.markdown(" **2.2 - From github geojson file of the city** ")


st.markdown("This data shows borders of the districts in Istanbul.")
#st.dataframe(jdf,500,150)

st.markdown("***For downloading this data to your desktop:***")

code ='''
cd desktop
git clone https://github.com/ozanyerli/istanbul-districts-geojson
''' 

st.code(code, language='python')


