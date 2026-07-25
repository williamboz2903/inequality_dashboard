from src.data_merge import DataMerge
from src.graphs import MyLineGraph
from src.data_clean import DataClean
from src.graphs import MyScatterPlot
from src.map import MyMap
from src.graphs import MyCovLineGraph


# This class is responsible for returning the correct list of graphs/maps/scatter plot 
# to be displayed fpr each statistics type
class GraphManager:

    def __init__(self, merge_data):
        self.merge_data = merge_data

    # This method calls up a line graph for one of the statistics
    # It shows both a line graph of the actual values , colour coded by region
    # It also displays a graph showing the coefficient of variation across the years for that statistic
    def get_line_graph(self, merge_data, statistic):
        graph_list = []
        if statistic == DataMerge.STATS_MEDIAN_PAY:
            pay_graph = MyLineGraph(DataMerge.STATS_MEDIAN_PAY, merge_data.merged, "Year", DataClean.median_pay_percent_change_colname , 
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

    # This method displays the correct scatter plot depending on the 
    # two statistics we wish to examine the correlation between
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

    # This method returns a list of maps 
    # The first map shows the % change for the statistic across each region from 2016
    # to a user selected year
    # The second map simply shows the values for each region in 2023 (latest year)
    def get_map(self, merge_data, statistic, year):
        map_list = []
        if year == 0:
            return map_list
        map_data = merge_data.get_data_for_year(year)
    
        map_data_latest = merge_data.get_data_for_year(2023)
        if statistic == DataMerge.STATS_MEDIAN_PAY:
            map1 = MyMap(map_data, DataClean.median_pay_percent_change_colname , """% change since 2016""" , 
                         ("""% change in annual median gross pay from 2016 to """ + str(year)))
            map_list.append(map1)
            map1_latest = MyMap(map_data_latest, DataClean.median_pay_colname, "Median pay for regions in 2023",
                                "Annual median gross pay in 2023 across UK regions")
            map_list.append(map1_latest)
            return map_list
        elif statistic == DataMerge.STATS_INACTIVITY:
            map2 = MyMap(map_data, DataClean.inactivity_percent_change_colname , """% change since 2016""" 
                         , """ % change in economic inactivity rate from 2016 to """ + str(year))
            map_list.append(map2)
            map2_latest = MyMap(map_data_latest, DataClean.inactivity_colname,
            "Inactivity for regions in 2023" ,
            "Economic inactivity rate in 2023 across Uk regions"
            )
            map_list.append(map2_latest)
            return map_list
        elif statistic == DataMerge.STATS_EDUCATION:
            map3 = MyMap(map_data, DataClean.education_colname)
            map_list.append(map3)
            return map_list
        else:
            return map_list


