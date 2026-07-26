import streamlit as st 
from src.data_merge import DataMerge

# This class is used to give the user a sidebar menu to select in streamlit for the graphs/data they want to view
# it makes use of empty containers called placeholders to give context sensitive menu options
class MyMenu:

    GRAPH_TYPE_NONE = 0
    GRAPH_TYPE_LINE = 1
    GRAPH_TYPE_SCATTER_PLOT = 2
    GRAPH_TYPE_MAP = 3

    YEAR_CHOICES_DEFAULT = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"] 
    # This constructor sets the value of each of the menu options to an empty string
    def __init__(self):
        self.graph_type = ""
        self.statistic = "" 
        self.scatter_selection = ""
        self.year_selection = ""
    
    #This method handles the display of the streamlit sidebar menu
    def show(self):
        st.sidebar.title("Customise")
        self.graph_type = st.sidebar.selectbox(
            "Choose an option",
        ["Line Graph", "Scatter Plot", "Map"])
        
        #Only display the individual statistics choices if we are not doing a scatter plot
        placeholder = st.sidebar.empty()

        if self.graph_type == "Scatter Plot":
            placeholder.empty()
        else:
             self.statistic = placeholder.selectbox(
            "Choose a statistic",
            ["Median Pay", "Inactivity", "Productivity"])


        #Only display the choice of correlation between statistics if we have chosen the scatter plot
        scatter_placeholder = st.sidebar.empty()

        if self.graph_type != "Scatter Plot":
            scatter_placeholder.empty()
        else:
            self.scatter_selection = st.sidebar.selectbox(
            "Choose a scatter plot",
            ["Median Pay vs Productivity", "Median Pay vs Inactivity"])

        #Only display a choice of year if looking at map
        year_placeholder = st.sidebar.empty()

        if self.graph_type == "Map":
            default_year = "2023"
            self.year_selection = st.sidebar.selectbox(
            "Choose a Year",
            MyMenu.YEAR_CHOICES_DEFAULT,
            index = MyMenu.YEAR_CHOICES_DEFAULT.index(default_year))
            
        else:
            year_placeholder.empty()
        
    # Used for debugging
    def get_selections(self):
        return  "graph_type: " + self.graph_type  + " statistic: " + self.statistic + " scatter_selection :" + self.scatter_selection + " year_selection :" + self.year_selection

    #This method translates the graph type string retunred from the streamnlit select box
    # into a constant class attribute
    def get_graph_type(self):
        if self.graph_type == "Map":
            return MyMenu.GRAPH_TYPE_MAP
        elif self.graph_type == "Line Graph":
            return MyMenu.GRAPH_TYPE_LINE
        elif self.graph_type == "Scatter Plot":
          return MyMenu.GRAPH_TYPE_SCATTER_PLOT       
        else:
            return MyMenu.GRAPH_TYPE_NONE
    
    #This method translates the statistic string retunred from the streamnlit select box
    # into a constant class attribute
    def get_graph_statistic(self):
        if self.statistic == "Median Pay":
            return DataMerge.STATS_MEDIAN_PAY
        elif self.statistic == "Inactivity":
            return DataMerge.STATS_INACTIVITY
        elif self.statistic == "Productivity":
            return DataMerge.STATS_PRODUCTIVITY
        else:
            return DataMerge.STATS_NONE
    
    #This method translates the correlation string retunred from the streamnlit select box
    # into a constant class attribute
    def get_scatter_plot_type(self):
        if self.scatter_selection == "Median Pay vs Inactivity":
            return DataMerge.SCATTER_PLOT_PAY_VS_INACTIVITY
        elif self.scatter_selection == "Median Pay vs Productivity":
            return DataMerge.SCATTER_PLOT_PAY_VS_PRODUCTIVITY
        else:
            return DataMerge.SCATTER_PLOT_NONE
        
    #This method translates the year string retunred from the streamnlit select box
    # into an integer , we return 0 if no year is selected , or the year select box is not displayed
    def get_year(self):
        if self.year_selection == "None":
            return 0
        elif self.year_selection == "":
            return 0
        else:
            return int(self.year_selection)