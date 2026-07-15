import streamlit as st 
import pandas as pd 
import plotly.express as px #
from src.data_raw import DataRaw
from src.data_clean import DataClean
from src.data_merge import DataMerge
from src.graphs import MyLineGraph
from src.graphs import MyScatterPlot

#Example data 
df = pd.DataFrame({ "Year": [2020, 2021, 2022, 2023, 2024],
                    "Inflation": [0.9, 2.5, 9.1, 6.8, 3.2] }) 

st.title("Economic Dashboard") 

fig = px.line( df, x="Year", y="Inflation", title="Inflation" ) 

#st.plotly_chart(fig) 

#loads the raw data
raw_data = DataRaw()
raw_data.load()

#cleans up the data 

clean_data = DataClean(raw_data)
clean_data.clean()

merge_data = DataMerge(clean_data)
merge_data.merge()
#st.write(merge_data.merged)

pay_graph = MyLineGraph(DataMerge.STATS_MEDIAN_PAY, merge_data.merged, "Year", DataClean.median_pay_colname , 
                                   "Region", DataClean.median_pay_title)

st.plotly_chart(pay_graph.line_graph)


inactivity_graph = MyLineGraph(DataMerge.STATS_INACTIVITY , merge_data.merged, "Year", DataClean.inactivity_colname , 
                                   "Region", DataClean.inactivity_title)

st.plotly_chart(inactivity_graph.line_graph)


education_graph = MyLineGraph(DataMerge.STATS_EDUCATION , merge_data.merged, "Year", DataClean.education_colname , 
                                   "Region", DataClean.education_title)

st.plotly_chart(education_graph.line_graph)

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


#st.write("hello world")
#st.write(clean_data.median_pay)
#st.write(clean_data.inactivity)
#st.write(clean_data.education)
#st.write(merge_data.merged)