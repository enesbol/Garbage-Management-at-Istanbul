# Garbage-Management-at-Istanbul
 
 https://enesbol-garbage-management-at-istanbul-homepage-chvayh.streamlitapp.com/

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://enesbol-garbage-management-at-istanbul-homepage-chvayh.streamlitapp.com/)

## Description

Project aims to identify priority areas where new garbage facilities, garbage recycling plants or other garbage-related facilities should be built.

## Conclusion
According to the results, this number is expected to reach by an increase of 10.7574% to 6.823m in 2022 in Istanbul, where the garbage production in 2021 is 6.161 m tons.
It has been found that the provinces that will be most affected by the garbage problem will be Şile, Çatalca and Adalar, respectively.


## Data
#### 1-Datas From Istanbul Data Portal 

####1.1- Garbage mass according to districts

####1.2- Locations of the waste facilities

### 2-Datas From Open Sources ###

####2.1 - Locations of all district centers in Turkey


####2.2 - From github geojson file of the city####

For installing this data to your desktop:
cd desktop
git clone https://github.com/ozanyerli/istanbul-districts-geojson

**You can reach all of the datas from the datas folder.**


<h3 align="left">Project's Steps:</h3>

1-Estimation of the amount of garbage that Istanbul will produce in 2022 with XGBRegressor.

2-Clustering districts with KMeans by the features that I created myself with the data that I gathered
from open sources.

3-Through these clusters, it was estimated which regions should be given priority in garbage
management.

4-Which locations waste facilities or recycling facilities should be constructed in the future.

5-Results and the features that I created are represented on the layered dynamic maps with the web app.

6-Connected to Google Sheets API with Service Account and used it as database 

7-All of that project deployed to a multi page cloud based web app and used for a presentation.


