from src.data_merge import DataMerge


class MyAnalysis:
    ANALYSIS_STATS_MEDIAN_PAY = """This line graph illustrates the change in median annual gross pay across the regions of the UK between 2016 and 2023.
Across all the regions , we can see that median pay has grown across all regions , with most regions seeing an increase between £7000 and £8000 between 2016 to 2023.
It has to be noted this does not mean that people across the UK have become significantly wealthier in this time period. 
      
To start , median pay is a nominal measure which does not account for inflation. In real terms , peopl
Additionally , the use of a median simply finds the middle value between the lowest pay and the highest pay. We have no information about those

London obviously appears to be a significant outlier compared to the other regions of the UK. It often has an annual pay around £7000-8000 higher than the closest region , the South East. Part of this could be extreme outliers , with London obviously being the UK’s main global financial centre 

Surprisingly , in 2020 , during the pandemic , we see that median pay either only declined slightly or remained stagnant in certain regions.
"""
    ANALYSIS_STATS_INACTIVITY = "Analysis for stats inactivity"
    ANALYSIS_STATS_EDUCATION = "Analysis for education"

    ANALYSIS_PAY_VS_INACTIVITY = "Analysis for pay vs inactivity"
    ANALYSIS_PAY_VS_EDUCATION = "Analysis for pay vs education"
    ANALYSIS_INACTIVITY_VS_EDUCATION = "Analysis for inactivity vs education"

    def __init__(self, statistic, scatter_plot):
        self.scatter_plot = scatter_plot
        self.statistic = statistic

    def get_analysis(self):
        if self.statistic == DataMerge.STATS_MEDIAN_PAY:
            return MyAnalysis.ANALYSIS_STATS_MEDIAN_PAY
        elif self.statistic == DataMerge.STATS_INACTIVITY:
            return MyAnalysis.ANALYSIS_STATS_INACTIVITY
        elif self.statistic == DataMerge.STATS_EDUCATION:
            return MyAnalysis.ANALYSIS_STATS_EDUCATION
        elif self.scatter_plot == DataMerge.SCATTER_PLOT_PAY_VS_INACTIVITY:
            return MyAnalysis.ANALYSIS_PAY_VS_INACTIVITY
        elif self.scatter_plot == DataMerge.SCATTER_PLOT_PAY_VS_EDUCATION:
            return MyAnalysis.ANALYSIS_PAY_VS_EDUCATION
        elif self.scatter_plot == DataMerge.SCATTER_PLOT_INACTIVITY_VS_EDUCATION:
            return MyAnalysis.ANALYSIS_INACTIVITY_VS_EDUCATION
        else:
            return None

