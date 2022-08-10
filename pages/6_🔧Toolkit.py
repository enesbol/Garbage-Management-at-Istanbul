import streamlit as st

st.set_page_config(layout="wide", page_icon = "💪")


st.title('Tools that I used in this project')

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("Images/Toolkit/St logo.png")
    st.image("Images/Toolkit/PyNum_Logo.png")
    st.image("Images/Toolkit/Matplotlib_Logo.png")
    st.image("Images/Toolkit/gboost.png",width=200)

with col2:
    st.image("Images/Toolkit/Pandas_logo.png")
    st.image("Images/Toolkit/Geopandas_Logo.png")
    st.image("Images/Toolkit/Dev Tools/Jupyter_logo.png",width=200)
    
with col3:
    st.image("Images/Toolkit/Leafmap_Logo.png") 
    st.image("Images/Toolkit/Folium_Logo.png")
    st.image("Images/Toolkit/Plotly_LOGO.png")    
    st.image("Images/Toolkit/Scikit_learn_logo_small.png", width=180)
with col4:
    st.image("Images/Toolkit/Dev Tools/Anaconda_Logo.png",width=200)
    st.image("Images/Toolkit/Dev Tools/VsCodeLogo.png",width=150)
    st.image("Images/Toolkit/Dev Tools/GitHub-Logo.png")
    
st.title('Project Key Features')

st.markdown(" **Filling time related data with interpolation.** ")
st.markdown(" **Geospatial data visualizations.**")
st.markdown(" **Gathering data from open source.**")
st.markdown(" **Chorophlet and Heatmap visualizations.**")
st.markdown(" **Common data manipulation operations like drop reindex to_datetime merge, creating new columns.**")
st.markdown(" **Data visualization with plotly dynamic objects.**")
st.markdown(" **Deploying maps and plotly objects with streamlit.**")
st.markdown(" **Calculate the distance between 2 locations with haversine formula.** ")
