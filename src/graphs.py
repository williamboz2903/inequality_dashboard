import plotly.express as px

from src.data_merge import DataMerge


# This class allows us to plot a line graph using plotly express to show
# how each region compares for each statistic over the years
class MyLineGraph:
    def __init__(self, statsType ,df, xCol, yCol, colorCol, title):
        self.line_graph = px.line(df , x = xCol, y = yCol, 
                              color = colorCol ,
                    title = title )
        # This ensures we get whole years instead of half years
        self.line_graph.update_xaxes(
           dtick = 1 ,
           tickmode = "linear"
        )
    
 
#This class allows us to plot a line graph that shows the coefficient of variation for each statistic
# representing the range of values between the regions across the years 
class MyCovLineGraph:
    def __init__(self, statsType ,df, xCol, yCol, title):#
        title = title + " (Coefficient of Variation)"
        self.line_graph = px.line(df , x = xCol, y = yCol, 
                    title = title  )
        # This ensures we get whole years instead of half years
        self.line_graph.update_xaxes(
           dtick = 1 ,
           tickmode = "linear"
        )
    
        if statsType ==  DataMerge.STATS_EDUCATION:
            self.line_graph.update_xaxes(range=[2019, 2023])    

# This class will allow us to plot scatter plots between two of our economic statistics
# We will also draw a regression line which will allow us to see if there is any correlation between
# the economic statistics
#Calculating the ordinarly least squares("ols") does take a few seconds to perform
class MyScatterPlot:
     def __init__(self, statsType ,df, xCol, yCol, my_title):
        self.scatter_graph = px.scatter(df, x = xCol,
                     y = yCol ,  
                     trendline = "ols" , title = my_title)
   

    
      
 
  