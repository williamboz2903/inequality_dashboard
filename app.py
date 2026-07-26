import pandas as pd
import plotly.express as px
import streamlit as st

from src.analysis import MyAnalysis
from src.data_clean import DataClean
from src.data_merge import DataMerge
from src.data_raw import DataRaw
from src.graph_manager import GraphManager
from src.menu import MyMenu


#Gives a title on streamlit site
st.title("UK Regional Inequality Dashboard") 
st.set_page_config(layout="wide")

# loads the raw data from the ONS using DataRaw class
raw_data = DataRaw()
raw_data.load()

# cleans up the data using the DataClean class
clean_data = DataClean(raw_data)
clean_data.clean()

# merges the data using the DataMerge class to allow scatter plots
merge_data = DataMerge(clean_data)
merge_data.merge()

# Creates the sidebar menu options in streamlit
my_menu = MyMenu()
my_menu.show()

# Get the menu options chosen by the user
graph_type = my_menu.get_graph_type()
statistic = my_menu.get_graph_statistic()
scatter_plot = my_menu.get_scatter_plot_type()
year = my_menu.get_year()

# Use GraphManager to display the correct graph, depending on the options.
# We will display a blank graph if user hasn't entered sufficient info
graph_manager = GraphManager(merge_data)

#provides written economic analysis for chosen graph/map
analysis = MyAnalysis(statistic, scatter_plot)

if graph_type == MyMenu.GRAPH_TYPE_MAP:
  my_map_list = graph_manager.get_map_list(merge_data, statistic, year)
  for my_map in my_map_list:
    st.plotly_chart(my_map.map)
  if len(my_map_list) > 0:
    st.markdown(analysis.get_analysis())
elif graph_type == MyMenu.GRAPH_TYPE_LINE:
  my_line_graph_list = graph_manager.get_line_graph_list(merge_data, statistic)
  for my_graph in my_line_graph_list:
      st.plotly_chart(my_graph.line_graph)
  if len(my_line_graph_list) > 0:
    st.markdown(analysis.get_analysis())
elif graph_type == MyMenu.GRAPH_TYPE_SCATTER_PLOT:
  my_scatter_plot = graph_manager.get_scatter_plot(merge_data, scatter_plot)
  if my_scatter_plot is not None:
    st.plotly_chart(my_scatter_plot.scatter_graph)
    st.markdown(analysis.get_analysis())
elif graph_type == MyMenu.GRAPH_TYPE_BAR_CHART:
  my_bar_chart_list = graph_manager.get_bar_chart_list(merge_data, statistic, year)
  for my_bar_chart in my_bar_chart_list:
    st.plotly_chart(my_bar_chart.bar_chart)
  if len(my_bar_chart_list) > 0:
    st.markdown(analysis.get_analysis())
