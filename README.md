Sources of raw data for code:
 Uk regional median annual gross pay : (https://www.ons.gov.uk/filters/412e9c37-c103-4622-ab45-1efe6bf0d15b/dimensions)

 Uk regional economic inactivity rate : (https://www.ons.gov.uk/explore-local-statistics/indicators/economic-inactivity-rate)

 Uk regions , people aged 19 and over achieving a funded further education and skills learning aim, per 100,000 people,: (https://www.ons.gov.uk/explore-local-statistics/indicators/further-education-skills-learner-achievements)

 Class DataRaw created to be responsible for loading the raw csv data donwladed from the ONS which is held in file data/raw into pandas dataframes

 Class DataClean is responsible for removing unnecessary columns from the pandas dataframe , realigning years so each dataframe uses the same set of years 

 Class DataMerge is responsible for combining the 3 seperate dataframes into 1 unified pandas dataframe which is used for generating the graphs

 Class MyLineGraph sets up the parameters needed to plot a pyplot line graph for any of the 3 pieces of data

 Class MyScatterPlot enables us to use 2 of the economic statistics and determine whether there is any form of correlation between them

Class MyMap uses a plotly express chloropleth map to display statistics geographically. It makes use of a geojson file
which describes each region as a complex polygon which is used by the map to display. 
The geojson file , rgn2025.geojson, is included in the project and was downloaded from the ONS

app.py is a streamlit app which displays all the data and possible graphs


Initially , there was an issue in merging the data frames. The median pay data had the region "East" for region code "E12000006" , while the inactivity and education data had the region "East of England" for the same region code. This prevetned this region code from being displayed in the merged data , so to fix this "East" was renamed to "East of England" in the cleaned median pay dataframe so the dtaaframes matched.

Added menu options to the main page

Added new class GraphManager to decide which graph to be displayed(none if the user has not entered sufficient information)

From the main app , use GraphManager to get the graph and display on streamlit if valid

When loading scatter plots , there will be a few seconds of delay while the regression line is calculated


I produced this project using Visual Studio Code and made use of Jupyter notebook plugin to act as a prototype for the project before rearranging it into separate python classes