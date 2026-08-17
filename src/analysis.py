from src.data_merge import DataMerge


class MyAnalysis:
    ANALYSIS_STATS_MEDIAN_PAY = ""
    
    ANALYSIS_STATS_INACTIVITY = ""

    ANALYSIS_STATS_PRODUCTIVITY = ""
    

    ANALYSIS_PAY_VS_INACTIVITY = """This scatter plot has a regression line that slopes downwards , indicating that there is a weak negative correlation.This implies that as median pay increases
    , the rate of economic inactivity falls. This seems to support traditional economic theory. Logically, higher wages  should incentivise people to seek employment rather than remain economically inactive. This is because with a higher wage, the opportunity cost of not working rises. As such, this should lead to more people entering the workforce in order to receive these higher wages, which should leave them with significantly more income than remaining inactive and on benefits with which they can increase their utility by having a higher income that can shift their budget constraint(the possible goods that can be purchased given a set income) outwards, which should lead to higher welfare as it is assumed more is preferred to less. Therefore, the negative correlation between the median pay and economic inactivity rate seems to support this logic.

Nonetheless , we have to be careful with drawing conclusions. To start with , the majority of the scatter points are between a median pay of £20000-£25000. We have very few scatter points for the higher ranges of median oay. Due to this , this correlation isn’t completely reliable due to a low sample size of data for higher median pay values above £30000. This is compounded by the fact that we only have 8 years of data, so it is difficult to suggest that with so few years to test this correlation, there is a definitive link between the two variables.

Furthermore , the correlation itself is fairly weak . We can likely argue that this suggests there are other reasons why the inactivity rate of certain regions may be higher than others than just different levels of median pay. For instance , it has been suggested in recent years that following Covid , there has been a significant rise in long-term sickness , which prevents people from re-entering the workforce. This might suggest that low wages may not necessarily be the main cause for certain regions having higher economic inactivity rates, and other factors can have significant impacts.

Ultimately, while we may be tempted to use this scatter plot to infer that one way to rescue the UK’s high economic inactivity rate is to try and increase median wages, our low sample size and relatively weak correlation means that this argument is not very reliable.
"""

    ANALYSIS_PAY_VS_PRODUCTIVITY = """This scatter plot has a regression line with a steep upwards slope , indicating a strong positive correlation between median pay and productivity. Economic theory argues that a rise in productivity , which raises the amount of output a firm can produce holding all other inputs constant , should result in firms paying higher wages to their employees. Consequently , we would expect there to be a strong positive correlation , which the data we have seems to support.

Additionally , there don’t appear to be any obvious outliers on the scatter plot. Although we have very few scatter points for median pay above £30000 , the points we do have still follow the general correlation.

Given the fact the correlation is so strong , while there are likely to be a range of factors that affect the levels of median pay , it seems that improving productivity levels is very likely to lead to a rise in median wages across the UK’s regions. 

If the productivity of a worker rises , that means that if we hold all other inputs constant , the value of output produced in a given time period will have increased. This increases the material benefit the firm receives for employing a given worker, and the marginal product of labour (the extra output that a firm gets from hiring one extra worker) will rise. In order to receive more workers , the firm will need to increase their reservation wage(the minimum wage that makes a worker indifferent between accepting the job and staying unemployed). As a result of this , firms will be willing to offer a higher wage in order to employ sufficient workers to boost productivity. Hence , the correlation has logical ground supporting it.

Regardless , the correlation might not necessarily imply the two are directly linked variables. 
As stated earlier, given we have so few scatter points above £30000, 
For instance, due to inflation reducing the value of real wages, workers may demand increases to their wages on the risk of strike action in order to prevent a decrease in their purchasing power. As such , the firm may be forced to pay higher wages to their workers, but their productivity may not have increased.
Additionally, the last few years have seen a severe rise in the usage of artificial intelligence, with many predicting it will lead to large rises in productivity.Yet, in spite of the fact it’s usage over the last years has been increasing, with more firms reducing the size of their workforces, we have not seen large rises in wages, implying that for certain technological improvements the correlation may not hold.

Ultimately, while we definitely need to be aware of some potential problems with the scatter plot, such as the low sample size and possibility of other factors, the strength of the correlation suggests it might be reasonable to suggest that a rise in productivity does correspond to a rise in the median wage.
"""

    def __init__(self, statistic, scatter_plot):
        self.scatter_plot = scatter_plot
        self.statistic = statistic

    def get_analysis(self):
        if self.statistic == DataMerge.STATS_MEDIAN_PAY:
            return MyAnalysis.ANALYSIS_STATS_MEDIAN_PAY
        elif self.statistic == DataMerge.STATS_INACTIVITY:
            return MyAnalysis.ANALYSIS_STATS_INACTIVITY
        elif self.statistic == DataMerge.STATS_PRODUCTIVITY:
            return MyAnalysis.AN
        elif self.scatter_plot == DataMerge.SCATTER_PLOT_PAY_VS_INACTIVITY:
            return MyAnalysis.ANALYSIS_PAY_VS_INACTIVITY
        elif self.scatter_plot == DataMerge.SCATTER_PLOT_PAY_VS_PRODUCTIVITY:
            return MyAnalysis.ANALYSIS_PAY_VS_PRODUCTIVITY
        else:
            return None

