import json
import pandas as pd
import plotly.express as px 
from src.data_merge import DataMerge


class MyMap:
    def __init__(self, df_year, stats_colName , my_label , my_title):
        with open("data/raw/rgn2025.geojson") as f:
            myGeoJson = json.load(f)
        self.map = px.choropleth(df_year, 
                    geojson= myGeoJson,
                    locations = "Region code" , 
                    featureidkey = "properties.Region_code", 
                    color = stats_colName ,
                    labels = { stats_colName : my_label}
                    )
        
        self.map.update_layout(title=my_title)

        self.map.update_geos(
         fitbounds = "locations" ,
         visible = False
         )