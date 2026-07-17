import json
import pandas as pd
import plotly.express as px 
from src.data_merge import DataMerge


class MyMap:
    def __init__(self, df_year, stats_colName ):
        with open("data/raw/rgn2025.geojson") as f:
            myGeoJson = json.load(f)
        self.map = px.choropleth(df_year, 
                    geojson= myGeoJson,
                    locations = "Region code" , 
                    featureidkey = "properties.Region_code", 
                    color = stats_colName
                    )
        
        myTitle = "Regional Inequality - " + stats_colName;
        self.map.update_layout(title=myTitle)

        self.map.update_geos(
         fitbounds = "locations" ,
         visible = False
         )