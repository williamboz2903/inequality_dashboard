import pandas as pd


# This class is responsible for loading pandas dataframes for each
# of the economic statistics analysed 
# All the raw data for these statistics was downloaded from the ONS 
# , and saved as CSV files in the project.
# The raw data is included in the project on GitHub 
class DataRaw:
    def load(self):
        self.median_pay = pd.read_csv("data/raw/regions_median_ashe_table_25.csv")
        self.inactivity = pd.read_csv("data/raw/economic-inactivity-rate-table.csv")
        self.productivity = pd.read_csv("data/raw/gross-value-added-per-hour-worked-table.csv")

