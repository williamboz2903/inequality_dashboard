import streamlit as st 
import pandas as pd 
import plotly.express as px 
from src.data_raw import DataRaw
from src.data_clean import DataClean
from src.data_merge import DataMerge
from src.menu import MyMenu
from src.graph_manager import GraphManager
from src.analysis import MyAnalysis


st.title("Economic Dashboard") 

# loads the raw data
raw_data = DataRaw()
raw_data.load()

# cleans up the data 
clean_data = DataClean(raw_data)
clean_data.clean()

# merges the data
merge_data = DataMerge(clean_data)
merge_data.merge()

#cov_df = merge_data.get_cov_for_statistic(DataMerge.STATS_MEDIAN_PAY)
#st.write(cov_df)

#my_line_graph = px.line(cov_df , x = "Year", y = "cov", 
                   # title = "Coefficient of variation" )
  
#st.plotly_chart(my_line_graph)
# Creates the Menu options
my_menu = MyMenu()
my_menu.show()

# Get the menu options chosen
graph_type = my_menu.get_graph_type()
statistic = my_menu.get_graph_statistic()
scatter_plot = my_menu.get_scatter_plot_type()
year = my_menu.get_year()

# st.write(my_menu.get_selections())
# st.write("Graph Type: " + str(graph_type))
# st.write("Statistic: " + str(statistic))
# st.write("Scatter Plot: " + str(scatter_plot))
# st.write("Year: " + str(year))

# Use GraphManager to display the correct graph, depending on the options.
# We will display a blank graph if user hasn't entered sufficient info
graph_manager = GraphManager(merge_data)

analysis = MyAnalysis(statistic, scatter_plot)

if graph_type == MyMenu.GRAPH_TYPE_MAP:
  my_map_list = graph_manager.get_map(merge_data, statistic, year)
  for my_map in my_map_list:
    st.plotly_chart(my_map.map)
  if len(my_map_list) > 0:
    st.markdown(analysis.get_analysis())
elif graph_type == MyMenu.GRAPH_TYPE_LINE:
  my_line_graph_list = graph_manager.get_line_graph(merge_data, statistic)
  for my_graph in my_line_graph_list:
      st.plotly_chart(my_graph.line_graph)
  if len(my_line_graph_list) > 0:
    st.markdown(analysis.get_analysis())
elif graph_type == MyMenu.GRAPH_TYPE_SCATTER_PLOT:
  my_scatter_plot = graph_manager.get_scatter_plot(merge_data, scatter_plot)
  if my_scatter_plot is not None:
    st.plotly_chart(my_scatter_plot.scatter_graph)
    st.markdown(analysis.get_analysis())
