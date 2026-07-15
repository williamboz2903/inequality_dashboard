import pandas as pd

class DataRaw:
    def load(self):
        self.median_pay = pd.read_csv("data/raw/regions_median_ashe_table_25.csv")
        self.inactivity = pd.read_csv("data/raw/economic-inactivity-rate-table.csv")
        self.education = pd.read_csv("data/raw/further_education.csv")
        
    