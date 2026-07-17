import pandas as pd

class DataClean:
  median_pay_title = "UK Regional Median Annual Gross Pay"
  median_pay_colname = "Median Pay"
  inactivity_title = "Economic inactivity percentage"
  inactivity_colname = "Inactivity"
  education_title = "Percentage of 19+ with further education skills"
  education_colname = "Education"

  def __init__(self, data_raw):
        self.raw_median_pay = data_raw.median_pay
        self.raw_inactivity = data_raw.inactivity
        self.raw_education = data_raw.education
    
  def clean(self):
      self.clean_median_pay() 
      self.clean_inactivity()
      self.clean_education()

  def clean_median_pay(self):
    self.median_pay = self.raw_median_pay[["v4_2", "Time", "administrative-geography" , "Geography" ]]

    self.median_pay = self.median_pay.rename(columns = {"v4_2" : DataClean.median_pay_colname})
    self.median_pay = self.median_pay.rename(columns = {"Time" : "Year"})
    self.median_pay = self.median_pay.rename(columns = {"Geography" : "Region"})
    self.median_pay = self.median_pay.rename(columns = {"administrative-geography" : "Region code"})
    self.median_pay.loc[self.median_pay["Region"] == "East", "Region"] = "East of England"

    self.median_pay = self.median_pay.sort_values(by = "Year")
  
  def clean_inactivity(self):
    self.inactivity = self.raw_inactivity[["areacd", "areanm", "period", "value"]]
    self.inactivity = self.inactivity.rename(columns = {"areacd" : "Region code"})
    self.inactivity = self.inactivity.rename(columns = {"areanm" : "Region"})
    self.inactivity = self.inactivity.rename(columns = {"period" : "Year"})
    self.inactivity = self.inactivity.rename(columns = {"value" : DataClean.inactivity_colname})
    self.inactivity["Year"] = self.inactivity["Year"].str[:4]
    self.inactivity["Year"] = self.inactivity["Year"].astype(int)
      
  def clean_education(self):
    self.education = self.raw_education.rename(columns= {"period" : "Year"})
    self.education = self.education.rename(columns = {"areanm": "Region"})
    self.education = self.education.rename(columns = {"areacd" : "Region code"})
    self.education = self.education.rename(columns = {"value" : DataClean.education_colname})

    self.education["Year"] = self.education["Year"].str[:4]
    self.education["Year"] = self.education["Year"].astype(int)
    self.education = self.education[~self.education["Year"].isin([2024])]

    self.education[DataClean.education_colname] = self.education[DataClean.education_colname] / 1000
     
  def get_data_for_year(self, df, year):
      filtered = df[df["Year"] == year]
      filtered = filtered.sort_values(by = "Region code")
      return filtered

