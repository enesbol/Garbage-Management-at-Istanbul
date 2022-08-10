
import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide", page_icon = "💪",initial_sidebar_state="collapsed")


st.title("Why Clustering")

st.markdown("I want to identfy a risk-level column with 6 independent variables. So I need to use an unsupervised machine learning model. The best model that fits my condition was KMeans.Therefore I used KMeans for labeling the data.")

with st.expander("Correlations"):

    code='''
# Visualize the correlation your data and identify variables for further analysis
g = sns.PairGrid(griddf)
g.map(sns.scatterplot);
'''
    st.code(code, language='python')
    st.image("Images/Kmeans/grid.png",width=600)




st.markdown("With all of my data that I collected from open source and Istanbul data portal I merged all of them in Main File. With  that columns I created a KMeans clusterig.")


st.title("Number of Clusters")

st.markdown("With WCSS, it was decided that the number of clusters should be 4.")



with st.expander("WCSS"):

    st.markdown("**Within Cluster Sum of Squares**")

    st.markdown("To calculate WCSS, you first find the Euclidean distance (see figure below) between a given point and the centroid to which it is assigned. You then iterate this process for all points in the cluster, and then sum the values for the cluster and divide by the number of points.")

    st.image("Images/Kmeans/wcss.png")


with st.expander("Display the Code"):
    code ='''
    #Determining number of the cluster.
    X = np.array(df.loc[:,['İlçe_Nüfusu',
    'Çöp_Ton_2021',
    'Çöp_Ton_2022',
    'Kişi_Başına_Çöp_Ton',
    'Min_Distance_to_Nearest_Facility',
    'Percetage_Change_Garbage']]).reshape(-1, 2)

    # Determine optimal cluster number with elbow method
    wcss = []
    sse = []

    for i in range(1, 11):
        model = KMeans(n_clusters = i,     
                        init = 'k-means++',                 # Initialization method for kmeans
                        max_iter = 300,                     # Maximum number of iterations 
                        n_init = 10,                        # Choose how often algorithm will run with different centroid 
                        random_state = 0)                   # Choose random state for reproducibility
        model.fit(X)                              
        wcss.append(model.inertia_)
        sse.append(model.inertia_)
    
    # Show Elbow plot

    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')                               # Set plot title
    plt.xlabel('Number of clusters')                        # Set x axis name
    plt.ylabel('Within Cluster Sum of Squares (WCSS)')      # Set y axis name
    plt.show()        
    
    ''' 
    st.code(code, language='python')

st.image("Images/Kmeans/Clusters (1).png")

st.markdown("Shilouette score graph was not good that much to take the value from it. So I used the classic elbow method.")

KMeansLabeled = pd.read_csv("Datas/KMeans/KMeans Labeled.csv")


st.title("First Result")

fig = px.scatter(KMeansLabeled, y="Min_Distance_to_Nearest_Facility", x="Percetage_Change_Garbage", color="k_means_pred",symbol="k_means_pred",hover_name="İlçe",width=1200, height=600)
fig.update_traces(marker_size=10)

fig.update_layout(xaxis_title='Percetage_Change_Garbage',
                  yaxis_title='Min_Distance_to_Nearest_Facility')

fig.update_layout(showlegend=False)
fig.update_layout(title_text='İstanbul İlçelerinin Sınıflara Göre Clusterları', title_x=0.46)

#st.plotly_chart(fig)


tab1, tab2, tab3 = st.tabs(["📈 Chart", "🗃 Data","📊 Code for Chart"])


tab1.subheader("Clusters")
tab1.plotly_chart(fig)

tab2.subheader("Labeled Data For Visualizating Clusters")
tab2.dataframe(KMeansLabeled)

tab3.subheader("Code for Chart")

code ='''import plotly.express as px


fig = px.scatter(df, y="Min_Distance_to_Nearest_Facility", x="Percetage_Change_Garbage", color="k_means_pred",symbol="k_means_pred",hover_name="İlçe",width=1100, height=600)
fig.update_traces(marker_size=10)

fig.update_layout(xaxis_title='Percetage_Change_Garbage',
                  yaxis_title='Min_Distance_to_Nearest_Facility')

fig.update_layout(showlegend=False)
fig.update_layout(title_text='İstanbul İlçelerinin Sınıflara Göre Clusterları', title_x=0.46)

fig.show() 
'''

tab3.code(code, language='python')


st.markdown("You may see the clustering results there. But as you see the labels are not separated that much good. It means you can't see the decomposition areas of the points.")

st.markdown("So I used **PCA** for creating new labels and representing the data according to them.")




st.title("PCA")

st.markdown("When you representing the data with 2 columns its easy to show and understanding the decomposition areas. But if you have 3 or more columns you need to use PCA or another dimension reduction algorithm for showing the results. PCA is a machine learning algorithm that gives you a chance to reduct your dimensions as I mentioned above.")

col1, col2 = st.columns(2)

with col1:
    st.image('Images/Kmeans/PCA1.png',caption=" 3D->2D ")
    

    st.image(
            "https://miro.medium.com/max/875/1*kG-ltJA_8cg5TtfPFz6cUA.gif", # I prefer to load the GIFs using GIPHY
             # The actual size of most gifs on GIPHY are really small, and using the column-width parameter would make it weirdly big. So I would suggest adjusting the width manually!
        )

with col2:
    st.image("Images/Kmeans/PCA2.png", caption=" Clusters ")



with st.expander("PCA"):
    #What is PCA
    st.markdown("Principal component analysis (PCA) is an unsupervised machine learning technique. Perhaps the most popular use of principal component analysis is dimensionality reduction. Besides using PCA as a data preparation technique, we can also use it to help visualize data.")

    
st.title("Final Result")

from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import numpy as np

Y = np.array(KMeansLabeled.loc[:,['İlçe_Nüfusu',
'Çöp_Ton_2021',
'Çöp_Ton_2022',
'Kişi_Başına_Çöp_Ton',
'Min_Distance_to_Nearest_Facility',
'Percetage_Change_Garbage']])
scaler=StandardScaler()
scaler.fit(Y)
scaled_data=scaler.transform(Y)
pca=PCA(n_components=2)
pca.fit(scaled_data)
x_pca=pca.transform(scaled_data)


fig = px.scatter(KMeansLabeled, y=x_pca[:,1], x=x_pca[:,0], color="k_means_pred",symbol="k_means_pred",hover_name="İlçe",width=1250, height=600)
fig.update_traces(marker_size=10)

fig.update_layout(xaxis_title='First principle component',
                  yaxis_title='Second principle component')

fig.update_layout(showlegend=False)
fig.update_layout(title_text='İstanbul İlçelerinin Sınıflara Göre Clusterları', title_x=0.46)


tab1, tab2, tab3 = st.tabs(["📈 Chart", "🗃 Code for PCA","📊 Code for Chart"])


tab1.subheader("Clusters after PCA")
tab1.plotly_chart(fig)

tab2.subheader("Code for PCA")
code ='''

from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
Y = np.array(df.loc[:,['İlçe_Nüfusu',
'Çöp_Ton_2021',
'Çöp_Ton_2022',
'Kişi_Başına_Çöp_Ton',
'Min_Distance_to_Nearest_Facility',
'Percetage_Change_Garbage']])
scaler=StandardScaler()
scaler.fit(Y)
scaled_data=scaler.transform(Y)
pca=PCA(n_components=2)
pca.fit(scaled_data)
x_pca=pca.transform(scaled_data)
scaled_data.shape
    
    ''' 
tab2.code(code, language='python')

tab3.subheader("Code for Chart")
code='''

import plotly.express as px

fig = px.scatter(df, y=x_pca[:,1], x=x_pca[:,0], color="k_means_pred",symbol="k_means_pred",hover_name="İlçe",width=1250, height=600)
fig.update_traces(marker_size=10)

fig.update_layout(xaxis_title='First principle component',
                  yaxis_title='Second principle component')

fig.update_layout(showlegend=False)
fig.update_layout(title_text='İstanbul İlçelerinin Sınıflara Göre Clusterları', title_x=0.46)

fig.show()

#Use this for displaying your plotly object in streamlit.
st.plotly_chart(fig)

'''

tab3.code(code, language='python')


