import streamlit as st 
import pandas as pd 
import plotly.express as px 

#Example data 
df = pd.DataFrame({ "Year": [2020, 2021, 2022, 2023, 2024],
                    "Inflation": [0.9, 2.5, 9.1, 6.8, 3.2] }) 

st.title("Economic Dashboard") 

fig = px.line( df, x="Year", y="Inflation", title="Inflation" ) 

st.plotly_chart(fig) 