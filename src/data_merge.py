import pandas as pd
from src.data_clean import DataClean

# The DataMerge class receives the cleaned data from DataClean in its contructor and then produces
# a single merged dataframe , which will contain all the economic statistics per year , per region, and per region code
# This is needed in order for us to be able to plot scatter plots to show any correlation between
# the statistics


class DataMerge:
    # These are the raw economic statistics we are analysing
    STATS_NONE = 0
    STATS_MEDIAN_PAY = 1
    STATS_INACTIVITY = 2
    STATS_PRODUCTIVITY = 3
    
    #These are the correlations between the statistics
    SCATTER_PLOT_NONE = 10
    SCATTER_PLOT_PAY_VS_INACTIVITY = 11
    SCATTER_PLOT_PAY_VS_PRODUCTIVITY = 12

    # We call these when plotting the scatter graphs
    title_pay_vs_inactivity = "Correlation between pay and inactivity"
    title_pay_vs_productivity = "Correlation between pay and productivity"

    def __init__(self, data_clean):
        self.median_pay = data_clean.median_pay
        self.inactivity = data_clean.inactivity
        self.productivity = data_clean.productivity
    
    #This method is responsible for merging the dataframes by "Year", "Region", and "Region Code"
    # For it to be merged successfully , each dataframe must have the same year , region code and region columns
    # At the end we sort by Year first , and then the other columns
    def merge(self):
        self.merged = pd.merge(self.median_pay, self.inactivity, 
                  on = ["Year", "Region code", "Region"])

        self.merged = pd.merge(self.merged, self.productivity, 
                          on = ["Year", "Region code", "Region"])
        self.merged = self.merged.sort_values(by = ["Year", "Region code", "Region"])

    # This method is used to just return the merged data fro a specific year 
    # This will be used when plotting maps
    def get_data_for_year(self, year):
        filtered_data = self.merged[self.merged["Year"] == year]
        filtered_data = filtered_data.sort_values(by = "Region code")
        return filtered_data
    
    #cov stands for Coefficient of Variation , a measure of the spread of data 
    # It is standard deviation / mean , which has been expressed as a percentage
    
    def get_cov_for_statistic(self , statistic):
        stats_colname = None
        if statistic == DataMerge.STATS_MEDIAN_PAY:
            stats_colname = DataClean.median_pay_colname
        elif statistic == DataMerge.STATS_INACTIVITY:
            stats_colname = DataClean.inactivity_colname
        elif statistic == DataMerge.STATS_PRODUCTIVITY:
            stats_colname = DataClean.productivity_colname
        # We have to return None if we do not give a valid stastistic parameter
        else:
            stats_colname = None
        
        if stats_colname is not None:
            # The .agg() function allows you to calculate both mean and standard deviation
            cov_df = ( 
                self.merged.groupby("Year")[stats_colname]
                .agg(
                Mean = "mean",
                StdDev = "std"
                )
            .reset_index() 
            )

            cov_df ["covraw"] = cov_df["StdDev"] / cov_df["Mean"]

            cov_df ["CV"] = cov_df["covraw"] * 100 

            return cov_df
        else:
            return None

        


        
