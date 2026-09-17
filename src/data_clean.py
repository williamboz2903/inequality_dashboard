import pandas as pd
import plotly.express as px
import streamlit as st


#This class is responsible for removing unnecessary columns from the raw data , standardising the column names
#in order to allow us to later merge the dataframes into one
# The common columns are "Year" , "Region", "Region code"
# Additionally , we calculate the percent change between a given year and the initial year for each region
# for each seperate dataframe

class DataClean:
  # These are class variables to store column names and titles for each of the statistics that 
  # are used throughout the project
  median_pay_title = "UK Regional Median Annual Gross Pay"
  median_pay_colname = "Median Pay"
  median_pay_percent_change_colname = """% change in median pay compared to 2016"""
  inactivity_title = "Economic inactivity percentage"
  inactivity_colname = "Inactivity"
  inactivity_percent_change_colname = """% change in inactivity rate compared to 2016"""
  productivity_title = "Labour productivity in £ per hour worked in the UK"
  productivity_colname = "Productivity"
  productivity_percent_change_colname = """% change in productivity compared to 2016"""

  # This constructor takes the DataRaw object which holds the raw pandas dataframes#
  # This stores a copy locally in this class
  def __init__(self, data_raw):
        self.raw_median_pay = data_raw.median_pay
        self.raw_inactivity = data_raw.inactivity
        self.raw_productivity = data_raw.productivity

  # This method is called from outside the class to initiate the cleaning of the data that is performed in the 
  # rest of this class
  def clean(self):
      self.clean_median_pay() 
      self.clean_inactivity()
      self.clean_productivity()

  # This method takes the raw data for Uk Median Regional Annual Gross Pay 
  # First , we select only specific columns that we need such as "Time" and "Geography"
  # Second , we rename these columns so that we can call them more easily and so their 
  # names are equivalent to the column names of the other dataframes , later allowing us to merge them.
  # e.g We use column names "Year" , "Region" , "Region code"
  # Specifically in the Median Pay dataframe , there is an issue where the East of England region is called
  # "East" , but in the other dataframes called "East of £ngalnd".
  # To ensure the data can be successfuly merged , we must rename this to "East of England".
  # We then sort all the values by ascending year.
  def clean_median_pay(self):
    self.median_pay = self.raw_median_pay[["v4_2", "Time", "administrative-geography" , "Geography" ]]

    self.median_pay = self.median_pay.rename(columns = {"v4_2" : DataClean.median_pay_colname})
    self.median_pay = self.median_pay.rename(columns = {"Time" : "Year"})
    self.median_pay = self.median_pay.rename(columns = {"Geography" : "Region"})
    self.median_pay = self.median_pay.rename(columns = {"administrative-geography" : "Region code"})
    self.median_pay.loc[self.median_pay["Region"] == "East", "Region"] = "East of England"
    

    # This section is used to create a series that shows the initial pay across each region
    # This intial pay is then used to calculate the percentage change difference 
    # from the starting year for different year
    # We will later plot this data on a map
    self.median_pay = self.median_pay.sort_values(["Region code", "Year"])
    # Get the first year's value for each region
    initial_pay = self.median_pay.groupby("Region code")[DataClean.median_pay_colname].transform("first")
    # Calculates cumulative % change from original year
    self.median_pay[DataClean.median_pay_percent_change_colname]  = (
       (self.median_pay[DataClean.median_pay_colname] - initial_pay) / initial_pay  * 100
    ).round(2)

    self.median_pay = self.median_pay.sort_values(by = "Year")
  
  # This method takes the raw data for Uk regional economic inactivity
  # First , we select only specific columns that we need
  # Second , we rename these columns so that we can call them more easily and so their 
  # names are equivalent to the column names of the other dataframes , later allowing us to merge them.
  # e.g We use column names "Year" , "Region" , "Region code"
  # With this dataframe , the year was included a day and a month , so we simplified to just represent 
  # the year for consistency with the other dataframes and allowing us to merge them.
  # This dataframe started at 2004 , so we have to ammend it so it starts at 2016
  # to allow us to later merge it with the other dataframes
  # We then sort all the values by ascending year


  def clean_inactivity(self):
    self.inactivity = self.raw_inactivity[["areacd", "areanm", "period", "value"]]
    self.inactivity = self.inactivity.rename(columns = {"areacd" : "Region code"})
    self.inactivity = self.inactivity.rename(columns = {"areanm" : "Region"})
    self.inactivity = self.inactivity.rename(columns = {"period" : "Year"})
    self.inactivity = self.inactivity.rename(columns = {"value" : DataClean.inactivity_colname})
    self.inactivity["Year"] = self.inactivity["Year"].str[:4]
    self.inactivity["Year"] = self.inactivity["Year"].astype(int)
    self.inactivity = self.inactivity[~self.inactivity["Year"].isin([2004, 2005, 2006, 2007, 2008
                                                                     , 2009, 2010, 2011, 2012, 2013, 2014
                                                                     , 2015
                                                                     ])]

    
    # This section is used to create a series that shows the initial inactivity across each region
    # This intial inactivity is then used to calculate the percentage change difference 
    # from the starting year for different year
    # We will later plot this data on a map

    self.inactivity = self.inactivity.sort_values(["Region code", "Year"])
    # Get the first year's value for each region
    initial_inactivity = self.inactivity.groupby("Region code")[DataClean.inactivity_colname].transform("first")
    # Calculates cumulative % change from original year
    self.inactivity[DataClean.inactivity_percent_change_colname]  = (
       (self.inactivity[DataClean.inactivity_colname] - initial_inactivity) / initial_inactivity  * 100
    ).round(2)


    self.inactivity = self.inactivity.sort_values(by = "Year")


  def clean_productivity(self):
    self.productivity = self.raw_productivity.rename(columns = {"areacd" : "Region code"})
    self.productivity = self.productivity.rename(columns = {"areanm" : "Region"})
    self.productivity = self.productivity.rename(columns = {"period" : "Year"})
    self.productivity = self.productivity.rename(columns = {"value" : DataClean.productivity_colname})
    self.productivity["Year"] = self.productivity["Year"].str[:4]
    self.productivity["Year"] = self.productivity["Year"].astype(int)
    self.productivity = self.productivity[~self.productivity["Year"].isin([2004, 2005, 2006, 2007, 2008
                                                                        , 2009, 2010, 2011, 2012, 2013, 2014
                                                                        , 2015
                                                                        ])]
    
    # This section is used to create a series that shows the initial productivity across each region
    # This intial productivity is then used to calculate the percentage change difference 
    # from the starting year for different year
    # We will later plot this data on a map
    self.productivity = self.productivity.sort_values(["Region code", "Year"])
    # Get the first year's value for each region
    initial_productivity = self.productivity.groupby("Region code")[DataClean.productivity_colname].transform("first")
    # Calculates cumulative % change from original year
    self.productivity[DataClean.productivity_percent_change_colname]  = (
       (self.productivity[DataClean.productivity_colname] - initial_productivity) / initial_productivity  * 100
    ).round(2)

    self.productivity = self.productivity.sort_values(by = "Year")