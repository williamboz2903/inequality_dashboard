from src.data_merge import DataMerge
from src.graphs import MyLineGraph
from src.data_clean import DataClean
from src.graphs import MyScatterPlot
from src.map import MyMap
from src.graphs import MyCovLineGraph
from src.graphs import MyBarChart


# This class is responsible for returning the correct list of graphs/maps/scatter plot 
# to be displayed fpr each statistics type
class GraphManager:

    def __init__(self, merge_data):
        self.merge_data = merge_data

    # This method calls up a line graph for one of the statistics
    # It shows both a line graph of the actual values , colour coded by region
    # It also displays a graph showing the coefficient of variation across the years for that statistic
    def get_line_graph_list(self, merge_data, statistic):
        graph_list = []
        if statistic == DataMerge.STATS_MEDIAN_PAY:
            pay_graph = MyLineGraph(DataMerge.STATS_MEDIAN_PAY, merge_data.merged, "Year", DataClean.median_pay_colname , 
                                   "Region", DataClean.median_pay_title)
            graph_list.append(pay_graph)
            
            cov_df = self.merge_data.get_cov_for_statistic(DataMerge.STATS_MEDIAN_PAY)
            pay_graph_cov = MyCovLineGraph(DataMerge.STATS_MEDIAN_PAY, cov_df , "Year", "CV", DataClean.median_pay_title)
            graph_list.append(pay_graph_cov)
            return graph_list
        
        elif statistic == DataMerge.STATS_INACTIVITY:
            inactivity_graph = MyLineGraph(DataMerge.STATS_INACTIVITY , merge_data.merged, "Year", DataClean.inactivity_colname , 
                                   "Region", DataClean.inactivity_title)
            
            
            graph_list.append(inactivity_graph)
            cov_df = self.merge_data.get_cov_for_statistic(DataMerge.STATS_INACTIVITY)
            graph_cov = MyCovLineGraph(DataMerge.STATS_INACTIVITY, cov_df , "Year", "CV", DataClean.inactivity_title)
            graph_list.append(graph_cov)
            return graph_list

        elif statistic == DataMerge.STATS_PRODUCTIVITY:
            productivity_graph = MyLineGraph(DataMerge.STATS_PRODUCTIVITY, merge_data.merged, "Year", DataClean.productivity_colname , 
                                           "Region", DataClean.productivity_title)
            graph_list.append(productivity_graph)
                    
            cov_df = self.merge_data.get_cov_for_statistic(DataMerge.STATS_PRODUCTIVITY)
            productivity_graph_cov = MyCovLineGraph(DataMerge.STATS_PRODUCTIVITY, cov_df , "Year", "CV", DataClean.productivity_title)
            graph_list.append(productivity_graph_cov)
            return graph_list
        else:
            return graph_list

    # This method displays the correct scatter plot depending on the 
    # two statistics we wish to examine the correlation between
    def get_scatter_plot(self, merge_data, scatter_plot_type):
        if scatter_plot_type == DataMerge.SCATTER_PLOT_PAY_VS_INACTIVITY:
            scatter_plot = MyScatterPlot(DataMerge.SCATTER_PLOT_PAY_VS_INACTIVITY , merge_data.merged
                           , DataClean.median_pay_colname, DataClean.inactivity_colname, 
                            DataMerge.title_pay_vs_inactivity)
            return scatter_plot

        elif scatter_plot_type == DataMerge.SCATTER_PLOT_PAY_VS_PRODUCTIVITY:
                    scatter_plot = MyScatterPlot(DataMerge.SCATTER_PLOT_PAY_VS_PRODUCTIVITY , merge_data.merged
                                   , DataClean.median_pay_colname, DataClean.productivity_colname , 
                                    DataMerge.title_pay_vs_productivity)
                    return scatter_plot
        else:
            return None

    # This method returns a list of maps 
    # The first map shows the % change for the statistic across each region from 2016
    # to a user selected year
    # The second map simply shows the values for each region in 2023 (latest year)
    def get_map_list(self, merge_data, statistic, year):
        map_list = []
        if year == 0:
            return map_list
        map_data = merge_data.get_data_for_year(year)
    
        if statistic == DataMerge.STATS_MEDIAN_PAY:
            map_for_year = MyMap(map_data, DataClean.median_pay_colname, "Median pay for regions in " + str(year) ,
                                 "Annual median gross pay in " + str(year) + " across UK regions")
            map_list.append(map_for_year)

            if year != 2016:
                map_change = MyMap(map_data, DataClean.median_pay_percent_change_colname , """% change since 2016""" , 
                         ("""% change in annual median gross pay from 2016 to """ + str(year)))
                map_list.append(map_change)
            return map_list
        
        elif statistic == DataMerge.STATS_INACTIVITY:
            map2_for_year = MyMap(map_data, DataClean.inactivity_colname,
                    "Inactivity for regions in 2023" ,
                    "Economic inactivity rate in 2023 across Uk regions"
                    )
            map_list.append(map2_for_year)

            if year != 2016:
                map2_change = MyMap(map_data, DataClean.inactivity_percent_change_colname , """% change since 2016""" 
                         , """ % change in economic inactivity rate from 2016 to """ + str(year))
                map_list.append(map2_change)
           
            return map_list

        elif statistic == DataMerge.STATS_PRODUCTIVITY:
            map3_for_year = MyMap(map_data, DataClean.productivity_colname, "Productivity (GVA) for regions in 2023",
                                    "Productivity in 2023 across UK regions")
            map_list.append(map3_for_year)

            if year != 2016:
                map3_change = MyMap(map_data, DataClean.productivity_percent_change_colname , """% change since 2016""" , 
                                 ("""% change in productivity (GVA) from 2016 to """ + str(year)))
                map_list.append(map3_change)
            return map_list
        
        else:
            return map_list


    def get_bar_chart_list(self, merge_data, statistic, year):
        chart_list = []
        if year == 0:
            return chart_list
        chart_data = merge_data.get_data_for_year(year)
    
        if statistic == DataMerge.STATS_MEDIAN_PAY:
            chart_for_year = MyBarChart(chart_data, "Region" , DataClean.median_pay_colname ,
                                 "Annual median gross pay in " + str(year) + " across UK regions")

            chart_list.append(chart_for_year)

            if year != 2016:
                bar_change = MyBarChart(chart_data, "Region", DataClean.median_pay_percent_change_colname ,
                         ("""% change in annual median gross pay from 2016 to """ + str(year)))
                chart_list.append(bar_change)
            return chart_list
        
        elif statistic == DataMerge.STATS_INACTIVITY:
            chart2_for_year = MyBarChart(chart_data, "Region" , DataClean.inactivity_colname,
                    "Economic inactivity rate in " + str(year) + " across Uk regions"
                    )
            chart_list.append(chart2_for_year)

            if year != 2016:
                chart2_change = MyBarChart(chart_data, "Region", DataClean.inactivity_percent_change_colname 
                         , """ % change in economic inactivity rate from 2016 to """ + str(year))
                chart_list.append(chart2_change)
           
            return chart_list

        elif statistic == DataMerge.STATS_PRODUCTIVITY:
            chart3_for_year = MyBarChart(chart_data, "Region" , DataClean.productivity_colname, 
                                         "Productivity (GVA) for regions in " + str(year) + " across UK regions")
            chart_list.append(chart3_for_year)

            if year != 2016:
                chart3_change = MyBarChart(chart_data, "Region" , DataClean.productivity_percent_change_colname , 
                                 ("""% change in productivity (GVA) from 2016 to """ + str(year)))
                chart_list.append(chart3_change)
            return chart_list
        
        else:
            return chart_list



