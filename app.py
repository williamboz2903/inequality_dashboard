import json
import streamlit as st 
import pandas as pd 
import plotly
import plotly.express as px 
from src.data_raw import DataRaw
from src.data_clean import DataClean
from src.data_merge import DataMerge
from src.graphs import MyLineGraph
from src.graphs import MyScatterPlot
from src.map import MyMap


def draw_line_graphs(merge_data):
  pay_graph = MyLineGraph(DataMerge.STATS_MEDIAN_PAY, merge_data.merged, "Year", DataClean.median_pay_colname , 
                                   "Region", DataClean.median_pay_title)
  st.plotly_chart(pay_graph.line_graph)


  inactivity_graph = MyLineGraph(DataMerge.STATS_INACTIVITY , merge_data.merged, "Year", DataClean.inactivity_colname , 
                                   "Region", DataClean.inactivity_title)

  st.plotly_chart(inactivity_graph.line_graph)


  education_graph = MyLineGraph(DataMerge.STATS_EDUCATION , merge_data.merged, "Year", DataClean.education_colname , 
                                   "Region", DataClean.education_title)

  st.plotly_chart(education_graph.line_graph)

def draw_scatter_plots(merge_data):
    scatter_plot_1 = MyScatterPlot(DataMerge.SCATTER_PLOT_PAY_VS_INACTIVITY , merge_data.merged
                           , DataClean.inactivity_colname, DataClean.median_pay_colname , 
                            DataMerge.title_pay_vs_inactivity)

    scatter_plot_1 = MyScatterPlot(DataMerge.SCATTER_PLOT_PAY_VS_INACTIVITY , merge_data.merged
                            , DataClean.inactivity_colname, DataClean.median_pay_colname , 
                           DataMerge.title_pay_vs_inactivity)

    st.plotly_chart(scatter_plot_1.scatter_graph)

    scatter_plot_2 = MyScatterPlot(DataMerge.SCATTER_PLOT_PAY_VS_EDUCATION , merge_data.merged
                            , DataClean.education_colname, DataClean.median_pay_colname , 
                            DataMerge.title_pay_vs_education)

    st.plotly_chart(scatter_plot_2.scatter_graph)

    scatter_plot_3 = MyScatterPlot(DataMerge.SCATTER_PLOT_INACTIVITY_VS_EDUCATION , merge_data.merged
                            , DataClean.education_colname, DataClean.inactivity_colname , 
                            DataMerge.title_inactivity_vs_education)

    st.plotly_chart(scatter_plot_3.scatter_graph)


st.title("Economic Dashboard") 

#loads the raw data
raw_data = DataRaw()
raw_data.load()

#cleans up the data 
clean_data = DataClean(raw_data)
clean_data.clean()

#merges the data
merge_data = DataMerge(clean_data)
merge_data.merge()


#df1 = clean_data.get_data_for_year(clean_data.inactivity, 2021)
#st.write("inactivity")
#st.write(df1)

#df2 = clean_data.get_data_for_year(clean_data.education, 2021)
#st.write("education")
#st.write(df2)

#df3 = clean_data.get_data_for_year(clean_data.median_pay, 2021)
#st.write("Median pay")
#st.write(df3)

# Draw Line Graphs for all statistics
draw_line_graphs(merge_data)

# Draw Scatter Plots for all combinations of statistics
draw_scatter_plots(merge_data)

# Draw Maps
map_year = 2023
st.write("Year " + str(map_year))
map_data = merge_data.get_data_for_year(map_year)
map1 = MyMap(map_data, DataClean.median_pay_colname)
st.plotly_chart(map1.map, key="MyMap1")

map2 = MyMap(map_data, DataClean.inactivity_colname)
st.plotly_chart(map2.map)

map3 = MyMap(map_data, DataClean.education_colname)
st.plotly_chart(map3.map);





