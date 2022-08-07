from ast import stmt
import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")



st.title("1- 2021 Garbage Data")

st.markdown("I filtered the data with just district names and 2021 values.")

df = pd.read_excel("ilce-yl-baznda-evsel-atk-miktar.xlsx", engine = 'openpyxl')  
df=df[['İlçe (Disticts)','2021']]



with st.expander("See Code"):  
    
    code ='''
    #Read and rename the columns

    df=df[['İlçe (Disticts)','2021']]
    df.columns=['İlçe','ÇöpTon']
    ''' 
    st.code(code, language='python')

#Display dataframe
st.dataframe(df,700,170)






st.title("2- 2021 Population Data")
st.markdown("I get the 2021 population data for calculating the ton of garbage per people and using it for clustering.")

df = pd.read_excel("2021 Nüfus İlçelere Göre.xlsx")

#Display code
code ='''
#Change the value of the row to match in merge.
ilceyegorenufus = ilceyegorenufus.replace('Eyüpsultan','Eyüp', regex=True)
ilceyegorenufus.sort_values(by=['İlçe']).head(8)

''' 
st.code(code, language='python')

#Display dataframe
st.dataframe(df,700,170)




st.title("3- The 2 data merged.")

code ='''
oransaldf = df.merge(ilceyegorenufus, how='left', on='İlçe')

''' 
st.code(code, language='python')







st.title("4- Garbage data per capita was produced from these 2 data.")

oransaldfKişiBaşınaÇöp_ton = pd.read_csv("oransaldfKişiBaşınaÇöp_ton.csv")
code ='''
oransaldf['KişiBaşınaÇöp'] = oransaldf['ÇöpTon'] / oransaldf['İlçe Nüfusu']


''' 
st.code(code, language='python')

st.dataframe(oransaldfKişiBaşınaÇöp_ton,900,170)



st.title("5- Added location data of districts")


with st.expander("See Code"):  
    
    code ='''
#File was containing all of the districts for Turkey    .
#Filtered for Istanbul
#Drop some columns - reindexed
#String manipulations for standardizing the common column.

ilce = pd.read_csv("ilce.csv")
ilce = ilce.loc[ilce['il_plaka'] == 34]
ilce = ilce.reset_index()
ilce.drop(columns=['il_plaka','ilce_id','index'], inplace=True)
ilcetemiz = ilce.drop(columns=[ 'northeast_lat',
'northeast_lon',
'southwest_lat',
'southwest_lon'])
ilcetemiz.columns=['İlçe','LATITUDE','LONGTITUDE']
ilcetemizcoord = ilcetemiz.iloc[:,1:3]
ilcetemiz['İlçe'] = ilcetemiz['İlçe'].str.lower()
ilcetemiz['İlçe'] = ilcetemiz['İlçe'].str.capitalize()
sondf = oransaldf.merge(ilcetemiz, how='left')  
    ''' 
    st.code(code, language='python')


sondflatlon = pd.read_csv("sondflatlonxxx.csv")

st.dataframe(sondflatlon,700,170)


st.title("6- Waste facilities location data was read and edited .")

CopTesisleriKonum = pd.read_csv("CopTesisleriKonum.csv")



with st.expander("See Code"):  
    #Display code
    code ='''        
    #Replaced LATITUDE and LONGTITUDE columns places.
    #Drop Unnecesary columns

    df.drop(columns=['ADDRESS','STATUS','NEIGHBORHOOD_NAME','STATUS','LOCATED_REGION_NAME','LOCATED_REGION_ID','COUNTY_UAVT_CODE','NEIGHBORHOOD_UAVT_CODE'], inplace=True)
    listlongt = df['LONGTITUDE'].tolist()   
    df = df.drop(columns=['LONGTITUDE'])    
    df['LONGTITUDE'] = listlongt     
    ''' 
    st.code(code, language='python')


st.dataframe(CopTesisleriKonum,700,170)


st.title("7- Distance")

st.markdown("Since it is important data in calculating the priorities of the districts, the distance between each district center and the nearest waste facilities was found.")

st.markdown("I had a data about waste facilities positions, and I had a data that contains de district center locations.")

st.markdown("I decided to find the distance of the nearest waste facilities for every district center.")

st.markdown("I created an algorithm for that.")

st.markdown("Now we have the distance to nearest waste facilities data for every district.")

st.markdown("As I mentioned above I use that data as a train input to my KMeans model. I'm sure that data is one of the important data in my train data.")

st.markdown("The distance was calculated using the Haversine formula.")


with st.expander("See Code"):  

    code ='''
#Tuple list yapmak için
def tuplemerger(list1, list2):

merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
return merged_list
    
#İlçe merkezlerinin konumları

lst1 = sondf['LATITUDE'].tolist()
lst2 = sondf['LONGTITUDE'].tolist()

#Çöp arıtma tesislerinin konumları.
lstwas1 = df['LATITUDE'].tolist()
lstwas2 = df['LONGTITUDE'].tolist()

#2 listenin ilgili verilerini tuple olarak birleştirip elemanları tuple olan
#  liste dönen fonksiyon 
#İlçe merkezlerinin tuple hali
tupleofstates = tuplemerger(lst1, lst2)

#Çöp arıtma tesislerinin konumlarının tuple hali.
tupleoffacilities = tuplemerger(lstwas1, lstwas2)

import haversine as hs

#Her ilçe merkezi için tüm arıtma tesisleri ile arasındaki mesafeyi bulup 
# en kısa olanı ayrı bir listeye ekleyen döngü.
allofdistances=[]
for i in tupleofstates:
    listfordistance = []
    for j in tupleoffacilities:
        listfordistance.append(hs.haversine(i,j))
        
    allofdistances.append(min(listfordistance)) 

#İlk veri sonda kalacağı için ilgili listeyi ters çevirdim.
allofdistances = allofdistances[::-1] 

#Veride 3 ondalık olacak şekilde düzenledim.
allofdistancesthreedecimal=[]
for i in range(0,len(allofdistances)):
    i = "{:.3f}".format(allofdistances[i])
    allofdistancesthreedecimal.append(i)

#Üretilen bu veriyi df'e kolon olarak ekledim
sondf['MinDistancetoFacility'] = allofdistancesthreedecimal

#Kolon Object olarak eklendiği için floata çevirdim
sondf['MinDistancetoFacility'] = sondf['MinDistancetoFacility'].astype('float')  

    ''' 
    st.code(code, language='python')


    

#Buraya shortest path(yakından) ve longest path uzaktan olacak şekilde ekle


st.title("8- 2022 and Put all together")

st.markdown("Added data that created with regression")

st.markdown("All of the columns get ready for training.")

st.markdown("DataFrame before training: ")

ReadyForKmeans= pd.read_csv("ReadyForKmeans.csv")

 
st.dataframe(ReadyForKmeans,900,170)


st.markdown("I performed some pandas and excel operations for edit, filter, drop some columns, clean, and standardize the data")


