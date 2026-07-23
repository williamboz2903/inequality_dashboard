import pandas as pd
import plotly.express as px 
from src.data_merge import DataMerge

class MyLineGraph:
    def __init__(self, statsType ,df, xCol, yCol, colorCol, title):
        self.line_graph = px.line(df , x = xCol, y = yCol, 
                              color = colorCol ,
                    title = title )
        self.line_graph.update_xaxes(
           dtick = 1 ,
           tickmode = "linear"
        )
    
        if statsType ==  DataMerge.STATS_EDUCATION:
            self.line_graph.update_xaxes(range=[2019, 2023])
 
class MyCovLineGraph:
    def __init__(self, statsType ,df, xCol, yCol, title):#
        title = title + " (Coefficient of Variation)"
        self.line_graph = px.line(df , x = xCol, y = yCol, 
                    title = title  )

        self.line_graph.update_xaxes(
           dtick = 1 ,
           tickmode = "linear"
        )
    
        if statsType ==  DataMerge.STATS_EDUCATION:
            self.line_graph.update_xaxes(range=[2019, 2023])    


class MyScatterPlot:
     def __init__(self, statsType ,df, xCol, yCol, my_title):
        self.scatter_graph = px.scatter(df, x = xCol,
                     y = yCol ,  
                     trendline = "ols" , title = my_title)
   

    
      
 
  