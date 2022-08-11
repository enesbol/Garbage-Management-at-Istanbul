
import streamlit as st
import plotly.express as px
import pandas as pd 
import folium


st.set_page_config(layout="wide")


st.title("Regression for Garbage Data of Istanbul") 

st.title("Why I need the 2022 garbage data")
st.markdown("I need to reach the amount of garbage in 2022 because I want to cluster the districts according to their risk priorities, so I  need the data that will be predicted here. I will use the 2022 value as an independent variable for KMeans Clustering.")

st.markdown("Also, I need to calculate the % percentage change between 2021 and 2022 garbage produce data. And I will also use that data when I training my model for Clustering.Because I want to cluster the districts according to their risk priorities, so I   need the data that will be predicted here. I will use the 2022 value as an independent variable for KMeans Clustering.")


st.title("Data Filling")
    
st.markdown("Used Interpolation for filling the data because data was time-related so when filling the rows there would have to be an increase.")




#tab1, tab2, tab3 = st.tabs(["📈 Silivri", "🕜 Şile","📊 Code for Chart"])


#tab1.subheader("Interpolation on Silivri")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Before Interpolation")
    st.image('Images/Interpolation/Silivri Before Interpolation.png',caption="Before Interpolation")
    st.image('Images/Interpolation/catalca_before.png',caption="Before Interpolation")
    st.image('Images/Interpolation/Şile_before.png',caption="Before Interpolation")
    
with col2:
    st.subheader("After Interpolation")
    st.image("Images/Interpolation/Silivri After Interpolation.png",caption="After Interpolation")
    
    st.image("Images/Interpolation/catalca_after.png",caption="After Interpolation")
    
    st.image("Images/Interpolation/Şile_after2.png",caption="After Interpolation")

with st.expander("📈 Çatalca"):
    code='''
 df['Çatalca'] = df['Çatalca'].interpolate(method='linear', limit_direction='forward', axis=0)
 plt.figure(figsize=(8,5))    
plt.plot(df.index, df.Çatalca,)
plt.title('Çatalca After Interpolation', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Çatalca Garbage', fontsize=14)
plt.grid(True)
plt.savefig('catalca_after.png')
plt.show()

 '''    
    st.code(code, language='python') 


df= pd.read_csv('Datas/Regression/IstanbulToplam2022.csv')

figcop = px.line(df, x="Yıllar", y="Toplam",template="plotly_white",width=1170, height=600,markers=True)


figcop.update_layout(
title={
    'text': "İstanbul Yıllık Çöp Grafiği",
    'y':0.96,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})



tab1, tab2, = st.tabs(["📈 Chart", "🗃 Code"])


tab1.subheader("Yearly Garbage Data for Istanbul") 
tab1.plotly_chart(figcop)

tab2.subheader("Codes For Creating Chart")

code='''

df= pd.read_csv('IstanbulToplam2022.csv')

figcop = px.line(df, x="Yıllar", y="Toplam",template="plotly_white",width=600, height=600,markers=True)


figcop.update_layout(
title={
    'text': "İstanbul Yıllık Çöp Grafiği",
    'y':0.96,
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'})

st.plotly_chart(figcop)

'''
tab2.code(code, language='python')





code2 = '''
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

cols = df.columns
cols = cols.to_list()
#print(cols)

cols.remove('Date')

X = df['Date'].to_frame()

list=[]
for i in cols:
    y = df[i].to_frame()
    # Splitting
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.3, random_state = 42)
    model = LinearRegression()
    model.fit(train_X, train_y)
    data={'Date':[2022]}
    df2=pd.DataFrame(data)
    predd = model.predict(df2)
    list.append(predd)

'''

st.code(code2, language='python')
