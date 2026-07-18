import streamlit as st 
import pandas as pd 
import plotly.express as px 
from src.data_raw import DataRaw
from src.data_clean import DataClean
from src.data_merge import DataMerge
from src.menu import MyMenu
from src.graph_manager import GraphManager

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
graph_manager = GraphManager()

if graph_type == MyMenu.GRAPH_TYPE_MAP:
  my_map = graph_manager.get_map(merge_data, statistic, year)
  if my_map is not None:
    st.plotly_chart(my_map.map)
elif graph_type == MyMenu.GRAPH_TYPE_LINE:
  my_line = graph_manager.get_line_graph(merge_data, statistic)
  if my_line is not None:
    st.plotly_chart(my_line.line_graph)
elif graph_type == MyMenu.GRAPH_TYPE_SCATTER_PLOT:
  my_scatter_plot = graph_manager.get_scatter_plot(merge_data, scatter_plot)
  if my_scatter_plot is not None:
    st.plotly_chart(my_scatter_plot.scatter_graph)
