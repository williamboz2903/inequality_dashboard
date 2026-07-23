import streamlit as st
import pandas as px
from src.data_merge import DataMerge
from src.graphs import MyLineGraph
from src.data_clean import DataClean
from src.graphs import MyScatterPlot
from src.map import MyMap
from src.graphs import MyCovLineGraph

class GraphManager:


    def __init__(self, merge_data):
        self.merge_data = merge_data

    def get_line_graph(self, merge_data, statistic):
        graph_list = []
        if statistic == DataMerge.STATS_MEDIAN_PAY:
            pay_graph = MyLineGraph(DataMerge.STATS_MEDIAN_PAY, merge_data.merged, "Year", DataClean.median_pay_colname , 
                                   "Region", DataClean.median_pay_title)
            graph_list.append(pay_graph)
            
            cov_df = self.merge_data.get_cov_for_statistic(DataMerge.STATS_MEDIAN_PAY)
            pay_graph_cov = MyCovLineGraph(DataMerge.STATS_MEDIAN_PAY, cov_df , "Year", "cov", DataClean.median_pay_title)
            graph_list.append(pay_graph_cov)
            return graph_list
        
        elif statistic == DataMerge.STATS_INACTIVITY:
            inactivity_graph = MyLineGraph(DataMerge.STATS_INACTIVITY , merge_data.merged, "Year", DataClean.inactivity_colname , 
                                   "Region", DataClean.inactivity_title)
            
            
            graph_list.append(inactivity_graph)
            cov_df = self.merge_data.get_cov_for_statistic(DataMerge.STATS_INACTIVITY)
            graph_cov = MyCovLineGraph(DataMerge.STATS_INACTIVITY, cov_df , "Year", "cov", DataClean.inactivity_title)
            graph_list.append(graph_cov)
            return graph_list

        elif statistic == DataMerge.STATS_EDUCATION:
            education_graph = MyLineGraph(DataMerge.STATS_EDUCATION , merge_data.merged, "Year", DataClean.education_colname , 
                                   "Region", DataClean.education_title)
            graph_list.append(education_graph)
            cov_df = self.merge_data.get_cov_for_statistic(DataMerge.STATS_EDUCATION)
            graph_cov = MyCovLineGraph(DataMerge.STATS_EDUCATION, cov_df , "Year", "cov", DataClean.education_title)
            graph_list.append(graph_cov)
            return graph_list
        else:
            return graph_list
        
    def get_scatter_plot(self, merge_data, scatter_plot_type):
        if scatter_plot_type == DataMerge.SCATTER_PLOT_PAY_VS_INACTIVITY:
            scatter_plot = MyScatterPlot(DataMerge.SCATTER_PLOT_PAY_VS_INACTIVITY , merge_data.merged
                           , DataClean.inactivity_colname, DataClean.median_pay_colname , 
                            DataMerge.title_pay_vs_inactivity)
            return scatter_plot

        elif scatter_plot_type == DataMerge.SCATTER_PLOT_PAY_VS_EDUCATION:
            scatter_plot = MyScatterPlot(DataMerge.SCATTER_PLOT_PAY_VS_EDUCATION , merge_data.merged
                            , DataClean.education_colname, DataClean.median_pay_colname , 
                            DataMerge.title_pay_vs_education)
            return scatter_plot
        
        elif scatter_plot_type == DataMerge.SCATTER_PLOT_INACTIVITY_VS_EDUCATION:
            scatter_plot = MyScatterPlot(DataMerge.SCATTER_PLOT_INACTIVITY_VS_EDUCATION , merge_data.merged
                            , DataClean.education_colname, DataClean.inactivity_colname , 
                            DataMerge.title_inactivity_vs_education)
            return scatter_plot
        else:
            return None
    
    def get_map(self, merge_data, statistic, year):
        
        if year == 0:
            return None
        map_data = merge_data.get_data_for_year(year)
    
        if statistic == DataMerge.STATS_MEDIAN_PAY:
            map1 = MyMap(map_data, DataClean.median_pay_colname)
            return map1
        elif statistic == DataMerge.STATS_INACTIVITY:
            map2 = MyMap(map_data, DataClean.inactivity_colname)
            return map2
        elif statistic == DataMerge.STATS_EDUCATION:
            map3 = MyMap(map_data, DataClean.education_colname)
            return map3
        else:
            return None


