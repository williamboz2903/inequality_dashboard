import json

import plotly.express as px


# This class is used to0 allow us to display a map which shows each of the Uk's regions
# We will use it to show the values for the economic statistics for each region in 2023
# as a point of comparison to show regional inequality
# Additionally , we will use it to plot percent changes between a given year and an initial year for
# a chosen economic statistic to show how trends have changed for each region
class MyMap:
    def __init__(self, df_year, stats_colName , my_label , my_title):
        # Load the ONS Uk region geojson file to produce 
        # the geojson object required by plotly express
        with open("data/raw/rgn2025.geojson") as f:
            myGeoJson = json.load(f)

        min_value = df_year[stats_colName].min()
        max_value = df_year[stats_colName].max()

        # Use the plotly express choropleth map to 
        # plot the statistic given by stats colname and
        # gives the colour bar the title given by my_label
        # "Turbo" alters the colour scale used on the mpa to make the difference clearer
        self.map = px.choropleth(df_year, 
                    geojson= myGeoJson,
                    locations = "Region code" , 
                    featureidkey = "properties.Region_code", 
                    color = stats_colName ,
                    range_color=(min_value, max_value),
                    color_continuous_scale="Turbo",
                    labels = { stats_colName : my_label}
                    )
        # Adds a title to the map
        self.map.update_layout(title=my_title)
        # This part ensures we are shown only the Uk map instead of the world map which has no data
        self.map.update_geos(
         fitbounds = "locations" ,
         visible = False
         )