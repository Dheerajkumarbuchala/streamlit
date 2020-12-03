# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:42:20 2020

@author: B.Dheeraj Kumar
"""

import streamlit as st
import numpy as np
import pandas as pd


cities_info = pd.read_csv ("cities_r2.csv") #importing the data into cities_info
#cities_info

cities = cities_info['name_of_city'] #creating a table of cities
#cities

states = cities_info['state_name'] #creating a table of states
states = states.drop_duplicates()  #we are removing the duplicates
#states

#we started to crete the dataframes of the above tables

df1 = pd.DataFrame({
    'column-1':cities
    })

df2 = pd.DataFrame({
    'column-2':states
    })

df3 = pd.DataFrame({
    'column-3':['Location']
    })

#creating a side bar to select city
option1 = st.sidebar.selectbox(
    'Select any city',
    df1['column-1'])


if option1:
    option2 = st.sidebar.selectbox(
        'Select the correponding state',
        df2['column-2'])
    'You selected : ',option1
    'You selected : ',option2
    
    selected_city_info = cities_info.loc[(cities_info["name_of_city"]==option1)] #collecting the information of the city (selecting the row in which the city is present).
    statename = selected_city_info['state_name'] #take the city name for further comparision (this is in the form of table)
    #statename
    try:
        val = statename.values[0] #while in table we can't use it's value,so we are taking it into a variable 
        if val==option2:
            st.text('Do you Know what...Your selected city and state matched.')
            st.text('Do you want to know more about the city...then press the below button.')
            left_column1, right_column1 = st.beta_columns(2) #creating colums
            pressed1 = left_column1.button('Press me') #placing a button to press in left column
            if pressed1:
                option3 = right_column1.selectbox(
                    'Select your option',
                    df3['column-3'])
                'You selected : ',option3
                if (option3=='Location'):
                    locate = selected_city_info['location'].values[0]
                    'Location in lat and long : ',locate
            
        else:
            st.text('Sorry your selection of city and state is not correct...Pls try again')
    except IndexError:
        ''
#this is a checkbox (if selected it shows the table of data we used)
if st.sidebar.checkbox('Show dataframe'):
    'This is the total dataframe used and may help you to check the results and cross verify'
    cities_info