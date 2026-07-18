import streamlit as st 
from src.data_merge import DataMerge


class MyMenu:

    GRAPH_TYPE_NONE = 0
    GRAPH_TYPE_LINE = 1
    GRAPH_TYPE_SCATTER_PLOT = 2
    GRAPH_TYPE_MAP = 3

    YEAR_CHOICES_DEFAULT = ["None", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
    YEAR_CHOICES_EDUCATION = ["None", "2019", "2020", "2021", "2022", "2023"]

    def __init__(self):
        self.graph_type = ""
        self.statistic = "" 
        self.scatter_selection = ""
        self.year_selection = ""
    
    def show(self):
        st.sidebar.title("")
        self.graph_type = st.sidebar.selectbox(
            "Choose an option",
        ["None", "Line Graph", "Scatter Plot", "Map"])


        placeholder = st.sidebar.empty()

        if self.graph_type == "Scatter Plot":
            placeholder.empty()
        else:
             self.statistic = placeholder.selectbox(
            "Choose a statistic",
            ["None", "Median Pay", "Inactivity", "Education"])



        scatter_placeholder = st.sidebar.empty()

        if self.graph_type != "Scatter Plot":
            scatter_placeholder.empty()
        else:
            self.scatter_selection = st.sidebar.selectbox(
            "Choose a scatter plot",
   ["None", "Median Pay vs Inactivity", "Median Pay vs Education", "Inactivity vs Education"])


        year_placeholder = st.sidebar.empty()

        if self.graph_type == "Map":
            if self.statistic == "Education":
                self.year_selection = st.sidebar.selectbox(
            "Choose a Year",
             MyMenu.YEAR_CHOICES_EDUCATION)
            else:
                self.year_selection = st.sidebar.selectbox(
                "Choose a Year",
                MyMenu.YEAR_CHOICES_DEFAULT)
            
        else:
            year_placeholder.empty()
        

    def get_selections(self):
        return  "graph_type: " + self.graph_type  + " statistic: " + self.statistic + " scatter_selection :" + self.scatter_selection + " year_selection :" + self.year_selection

    def get_graph_type(self):
        if self.graph_type == "Map":
            return MyMenu.GRAPH_TYPE_MAP
        elif self.graph_type == "Line Graph":
            return MyMenu.GRAPH_TYPE_LINE
        elif self.graph_type == "Scatter Plot":
          return MyMenu.GRAPH_TYPE_SCATTER_PLOT       
        else:
            return MyMenu.GRAPH_TYPE_NONE
    

    def get_graph_statistic(self):
        if self.statistic == "Median Pay":
            return DataMerge.STATS_MEDIAN_PAY
        elif self.statistic == "Inactivity":
            return DataMerge.STATS_INACTIVITY
        elif self.statistic == "Education":
            return DataMerge.STATS_EDUCATION
        else:
            return DataMerge.STATS_NONE
        
    def get_scatter_plot_type(self):
        if self.scatter_selection == "Median Pay vs Inactivity":
            return DataMerge.SCATTER_PLOT_PAY_VS_INACTIVITY
        elif self.scatter_selection == "Median Pay vs Education":
            return DataMerge.SCATTER_PLOT_PAY_VS_EDUCATION
        elif self.scatter_selection == "Inactivity vs Education":
            return DataMerge.SCATTER_PLOT_INACTIVITY_VS_EDUCATION
        else:
            return DataMerge.SCATTER_PLOT_NONE
        
    
    def get_year(self):
        if self.year_selection == "None":
            return 0
        elif self.year_selection == "":
            return 0
        else:
            return int(self.year_selection)