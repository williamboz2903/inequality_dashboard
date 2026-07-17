import pandas as pd

class DataMerge:
    STATS_MEDIAN_PAY = 1
    STATS_INACTIVITY = 2
    STATS_EDUCATION = 3
    
    SCATTER_PLOT_PAY_VS_INACTIVITY = 4
    SCATTER_PLOT_PAY_VS_EDUCATION = 5
    SCATTER_PLOT_INACTIVITY_VS_EDUCATION = 6
    
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
