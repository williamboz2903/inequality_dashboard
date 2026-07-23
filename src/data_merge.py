import pandas as pd
from src.data_clean import DataClean

class DataMerge:
    STATS_NONE = 0
    STATS_MEDIAN_PAY = 1
    STATS_INACTIVITY = 2
    STATS_EDUCATION = 3
    
    SCATTER_PLOT_NONE = 4
    SCATTER_PLOT_PAY_VS_INACTIVITY = 5
    SCATTER_PLOT_PAY_VS_EDUCATION = 6
    SCATTER_PLOT_INACTIVITY_VS_EDUCATION = 7

    STATS_MEDIAN_PAY_STD = 8
    
    title_pay_vs_inactivity = "Correlation between pay and inactivity"
    title_pay_vs_education = "Correlation between pay and education"
    title_inactivity_vs_education = "Correlation between education and inactivity"

    def __init__(self, data_clean):
        self.median_pay = data_clean.median_pay
        self.inactivity = data_clean.inactivity
        self.education = data_clean.education
    
    def merge(self):
        self.merged = pd.merge(self.median_pay, self.inactivity, 
                  on = ["Year", "Region code", "Region"])
        
        self.merged = pd.merge(self.merged, self.education, 
                  on = ["Year", "Region code", "Region"], how = "left")
        self.merged = self.merged.sort_values(by = ["Year", "Region code", "Region"])
    
    def get_data(self):
        return self.merged
    
    def get_data_for_year(self, year):
        filtered_data = self.merged[self.merged["Year"] == year]
        filtered_data = filtered_data.sort_values(by = "Region code")
        return filtered_data
    
    #cov stands for Coefficient of Variation
    def get_cov_for_statistic(self , statistic):
        stats_colname = None
        if statistic == DataMerge.STATS_MEDIAN_PAY:
            stats_colname = DataClean.median_pay_colname
        elif statistic == DataMerge.STATS_INACTIVITY:
            stats_colname = DataClean.inactivity_colname
        elif statistic == DataMerge.STATS_EDUCATION:
            stats_colname = DataClean.education_colname
        else:
            stats_colname = None
        
        if stats_colname is not None:
            cov_df = ( 
                self.merged.groupby("Year")[stats_colname]
                .agg(
                Mean = "mean",
                StdDev = "std"
                )
            .reset_index() 
            )

            cov_df ["covraw"] = cov_df["StdDev"] / cov_df["Mean"]

            cov_df ["cov"] = cov_df["covraw"] * 100 

            return cov_df
        else:
            return None

        


        
