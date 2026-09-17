from src.data_merge import DataMerge


class MyAnalysis:
    ANALYSIS_STATS_MEDIAN_PAY = """ Raw data: https://www.ons.gov.uk/filters/412e9c37-c103-4622-ab45-1efe6bf0d15b/dimensions
    
This line graph illustrates the change in median annual gross pay across the regions of the UK between 2016 and 2023. Comparing the different areas, we can see that median pay has grown for  all of the regions, with most areas seeing an increase between £7000 and £8000 between 2016 to 2023.

The range (highest - lowest value) of the data in 2016 is around £10,500 (London - Wales). Compare this to 2023 where the range is £12000 . This suggests that actually the inequality in median pay has worsened over the selected timespan. 

There was stagnation in wage growth during Covid across most regions, and London actually saw a slight fall, likely due to the lockdown forcing firms to have to cut wages in order to avoid bankruptcy given many firms, particularly service sector industries, could not operate with lockdown restrictions, leading to lower median wages. However, in spite of the overall increase in the median pay, it has to be noted this does not mean that people across the UK have become significantly wealthier in this time period. 

Firstly, median pay is a nominal measure which does not account for inflation. In real terms, wages will not have risen by c£7000-£8000, particularly given the high rates of inflation in 2022 following the energy price shock, where it rose as high as 11.1%.[1] Some reports have stated that real wages have actually fallen in recent years, so this supposed rise in median wages does not allow us to immediately conclude real wages or living standards have risen in these past 8 years.

Additionally, the use of a median simply finds the middle value between the lowest pay and the highest pay. We have no information about the wage disparity between the highest and lowest earners. So if, for example, the poorest people have actually seen their pay fall, while the rest of the population’s pay has risen,  the median will still rise overall but we miss the fact that the inequality in pay between the highest and lowest earners has actually risen.

London obviously appears to be a significant outlier compared to the other regions of the UK. It often has an annual pay around £7000-8000 higher than the closest region, the South East. Part of this could be extreme outliers, with London obviously being the UK’s main global financial centre, and attracting high talent to the capital where often large, prestigious multinational firms are based, who offer high pay to employ people with skills in high demand and low supply. Of course, the higher median pay cannot immediately allow us to conclude that standards of living and general quality of life is higher in London compared to other regions. Firstly, the cost of living in London is significantly higher than most areas of the UK. The affordability ratio (house prices to earnings) of London is about 10.6 in 2025. In comparison, the North East’s average affordability ratio was 5.0 [2]. As such, although London may have the highest median pay, it may be suggested that given London’s affordability crisis, potentially people living in the North East may have more disposable income after accounting for taxes, food, rent and household bills.



Sources

[1] https://www.bbc.co.uk/news/articles/c17rgd8e9gjo
 
[2] https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/housingaffordabilityinenglandandwales/2025#housing-affordability-in-england-and-wales
"""

    ANALYSIS_COV_MEDIAN_PAY = """ The coefficient of variation (CV) acts as a measure of how spread out the data is. The higher the coefficient of variation, the greater the range in values above or below the mean value, which signals a higher level of regional inequality. It is calculated by taking the standard deviation and dividing it by the mean, giving us a ratio between the two.
For median pay, we see the coefficient of variation initially starting at about 13.4. Given that the main line graph already shows London as a significant outlier compared to the rest of the UK’s regions, this is unsurprising. Significantly, although we see a rise in the CV between 2016 to 2018, the general trend is a fall in the CV, decreasing to under 12 by 2023. 
However, we must be careful with what the coefficient of variation is expressing. It is simply the standard deviation / mean. Given the fact that the mean has risen over the time period, this means the denominator will be larger, and therefore lead to the value of the CV falling, even if the actual regional inequality remains the same or has actually worsened. As such, it is likely that the declining value of the CV does not indicate a fall in regional inequality for median pay, but rather just an effect of a change in the overall mean.
 """

    ANALYSIS_STATS_INACTIVITY = """ Raw data: https://www.ons.gov.uk/explore-local-statistics/indicators/economic-inactivity-rate

This line graph shows the rate of economic inactivity across each of the UK’s regions. 
Economic inactivity should not be confused with unemployment. The unemployment rate calculates the number of people who are out of work but searching for work as a proportion of the labour force (Employed + Unemployed). The economic inactivity rate measures the number of people out of work but NOT searching for new employment, often due to reasons such as caring responsibilities, long-term sickness or early retirement as a proportion of the total working age population. Recent reports have stated that the UK has 9.1 million people being classed as economically inactive in 2026. [1]

The inactivity rate across the years has been very volatile for all the regions. London, for instance, saw a 0.9% rise between 2022 and 2023. The West Midlands appears to have seen the most significant improvement, falling from an inactivity rate of 24.6% down to 21.2%. In comparison, the North East saw small rises and falls, and by 2023 it has only seen the inactivity rate decrease by 0.3%. This indicates there has not been uniformity in how each of the region’s inactivity rates have changed across the 8 year period. Potential reasons for this could be differences in educational achievement. Usually, we would expect that if a person is more educated, they will have more employment opportunities with higher wages compared to unskilled labour.

The graph does show that, with the exception of 2019-2020, the North East consistently had the highest rate of economic inactivity, peaking at 26% in 2022. One could make the argument that given the deindustrialisation that occurred primarily in North East England during the 1980s, as there was a sharp rise in unemployment, we might also expect to see a permanent increase in economic inactivity. Deindustrialisation resulted in more structurally unemployed workers, where they did not have sufficient skills to be able to transfer to say the growing service sector. If they remained unemployed for longer periods, they may have decided to give up on seeking a new job, resulting in them becoming economically inactive. The service sector is also primarily focused in London and the South East, so it is possible that geographical immobility of labour, where factors like poor transport links prevent workers from moving to new areas for employment, contributed to a consistently higher economic inactivity rate in the North East compared to the South East.

Sources

[1] https://commonslibrary.parliament.uk/the-uk-labour-market/

"""

    ANALYSIS_COV_INACTIVITY = """ Interestingly, we see that the coefficient of variation ranges between 9 and 10.5, 
substantially lower than the coefficients for median pay and productivity. 
This could therefore suggest that there is a lower regional inequality when it comes to the inactivity rate 
across the UK’s different regions. Yet, there is not a clear downwards trend for the CV, and it appears to be 
quite volatile between the years, so we cannot conclude with certainty that over the whole period the gap 
in economic inactivity between the regions has consistently been decreasing, rather it has varied a lot."""

    ANALYSIS_STATS_PRODUCTIVITY = """ Raw data: https://www.ons.gov.uk/explore-local-statistics/indicators/gross-value-added-per-hour-worked
    
This line graph shows the changes to labour productivity across each of the UK’s regions. Productivity is a measure of essentially how much output is produced in a given period of time. If we hold all of our inputs constant, but a worker’s productivity rises, output will increase despite no change in inputs. Higher productivity levels lead to more goods and services being produced by the economy, often leading to real GDP growth.
The data shows that broadly all of the regions experienced a gradual improvement in their levels of productivity between 2016 and 2023. Normally, economists tend to associate improvements to productivity as being down to perhaps improved skills training or reducing geographical immobility of labour (for example, improving transport infrastructure in rural areas so it is easier for people to access areas with better employment opportunities). Most importantly, a rise in the total factor productivity of the economy (z), which signifies technological progress, such as the implementation of artificial intelligence perhaps, is likely to cause significant productivity increases.

There have been numerous reports since the Global Financial Crisis in 2008 that the UK has a severe issue with productivity. Since 2008, UK productivity has effectively flatlined, with average productivity growth being 0.6% between 2009 to 2023. In contrast, between 1971-2007, UK productivity growth was 2.2% [1]. There have been a multitude of reasons, ranging from frequent economic shocks like Brexit and COVID to the short lifespan of recent governments, causing frequent policy changes that lead to uncertainty and thus lower levels of private sector investment.

The data shows that once again, London is a significant outlier, usually being around 9 points higher than the closest region, the South East.
Additionally, the range is quite large here. By the end of the period, the range was almost 19 points (London - Wales), having increased from around 17 points in 2016, indicating a very significant productivity gap. London’s productivity was 153% that of Wales by 2023, showing just how severe the inequality in productivity rates are across the UK’s regions. However, if we think about the sectors that compose these two regions, there is a clear explanation for why this is likely the case.
London acts as the UK’s financial centre and the main focus of multinational corporations. These are often sectors employing highly skilled workers who use large levels of capital like computers and artificial intelligence to boost their productivity. By contrast, Wales remains fairly agricultural, and is more reliant on sectors like tourism which do not use so much capital, likely leading to lower levels of productivity as there is a much lower ratio between labour and capital in these sorts of sectors. As a result of this, it is unsurprising the productivity gap is so large, indicating that there needs to be some effective Government policy if this regional inequality is to be reduced, as market forces do not seem to be capable of solving this issue.  

Sources:

[1] https://post.parliament.uk/economic-growth-and-productivity/

"""

    ANALYSIS_COV_PRODUCTIVITY = """ We see that the Coefficient of Variation (CV) initially starts 
at around 15.8 in 2016, but sees a steady decline across all years, falling to about 14.0 by 2023.
One could say that this should imply the productivity gap between the regions has lowered. Nonetheless,
similarly to median pay, it is perhaps more likely this fall is simply due to what the CV is actually
measuring. We have already seen that all regions have seen roughly equal actual changes in their 
productivity levels, increasing the mean productivity of the UK’s regions. As the CV simply states
the ratio of the standard deviation to the mean, due to the mean rising while the 
standard deviation remains about the same, the CV value will fall. Consequently, it 
is more likely the fall in the CV is due to this mathematical explanation, 
than an actual fall in the difference between the regions’ productivity levels."""
    

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

    RAW_DATA_MEDIAN_PAY = """Raw data: https://www.ons.gov.uk/filters/412e9c37-c103-4622-ab45-1efe6bf0d15b/dimensions
     """

    RAW_DATA_INACTIVITY = """Raw data: https://www.ons.gov.uk/explore-local-statistics/indicators/economic-inactivity-rate """

    RAW_DATA_PRODUCTIVITY = """Raw data: https://www.ons.gov.uk/explore-local-statistics/indicators/gross-value-added-per-hour-worked """
    
    def __init__(self, statistic, scatter_plot):
        self.scatter_plot = scatter_plot
        self.statistic = statistic

    def get_line_analysis(self):
        if self.statistic == DataMerge.STATS_MEDIAN_PAY:
            return MyAnalysis.ANALYSIS_STATS_MEDIAN_PAY
        elif self.statistic == DataMerge.STATS_INACTIVITY:
            return MyAnalysis.ANALYSIS_STATS_INACTIVITY
        elif self.statistic == DataMerge.STATS_PRODUCTIVITY:
            return MyAnalysis.ANALYSIS_STATS_PRODUCTIVITY
        else:
            return None

    def get_cov_analysis(self):
        if self.statistic == DataMerge.STATS_MEDIAN_PAY:
            return MyAnalysis.ANALYSIS_COV_MEDIAN_PAY
        elif self.statistic == DataMerge.STATS_INACTIVITY:
            return MyAnalysis.ANALYSIS_COV_INACTIVITY
        elif self.statistic == DataMerge.STATS_PRODUCTIVITY:
            return MyAnalysis.ANALYSIS_COV_PRODUCTIVITY
        else:
            return None

    def get_scatter_analysis(self):
        if self.scatter_plot == DataMerge.SCATTER_PLOT_PAY_VS_INACTIVITY:
            return MyAnalysis.ANALYSIS_PAY_VS_INACTIVITY
        elif self.scatter_plot == DataMerge.SCATTER_PLOT_PAY_VS_PRODUCTIVITY:
            return MyAnalysis.ANALYSIS_PAY_VS_PRODUCTIVITY
        else: return None


    def get_bar_or_map_analysis(self):
        if self.statistic == DataMerge.STATS_MEDIAN_PAY:
            return MyAnalysis.RAW_DATA_MEDIAN_PAY
        elif self.statistic == DataMerge.STATS_INACTIVITY:
            return MyAnalysis.RAW_DATA_INACTIVITY
        elif self.statistic == DataMerge.STATS_PRODUCTIVITY:
            return MyAnalysis.RAW_DATA_PRODUCTIVITY
        else:
            return None