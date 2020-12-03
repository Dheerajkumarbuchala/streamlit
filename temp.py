# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import numpy as np
import pandas as pd

st.title('My First app')
#this adds the title to our app.

# we can pass literally anything as an argument yo st.write()
st.write("Here's our first attempt at using data to create a table :")
# here we passed a text

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    }))
# here we passed a pandas dataframe as an argument

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
st.write("To check the functionality of st.dataframe :")
st.dataframe(df)
# to check the functionality of st.dataframe() 
#creates a table similar to what we created with write with additional features like colors

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.write("To check the functionality of st.line_chart :")
st.line_chart(chart_data)
#creates a line chart

map_data = pd.DataFrame(
    np.random.rand(1,2)/ [50, 50] + [28.644800, 77.216721],
    columns=['lat', 'lon'])
st.write("To check the functionality of st.map :")
st.map(map_data)
#creates a map

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    st.line_chart(chart_data)


option = st.selectbox(
    'Which number do you like best?',
     df['first column'])
'You selected: ', option



left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

