import pandas as pd
import streamlit as st
from libraries import *

countries = ['USA', 'Australia', 'China', 'Spain', 'Eygypt', 'Sri Lanka']
country_code = {"Sri Lanka" : "lk" , "United States" : "us" , "Australia" :"aus" , "Spain" : "esp","Egypt" : "egy" ,"China" :"cn"}
data_types = ['cases', 'deaths', 'recoveries']



country = st.sidebar.selectbox('Pick a country', countries)
days = st.sidebar.slider('Select number of days', min_value=1,max_value=90)
data_type = st.sidebar.multiselect('Pick data types', data_types)


cases_df = get_historic_cases(country,days)
deaths_df = get_historic_deaths(country,days)
recoveries_df = get_historic_recoveries(country,days)
historic_df = pd.concat([cases_df,deaths_df,recoveries_df],axis=1).astype(int)


daily_cases_df = get_daily_cases(country,days)
daily_deaths_df = get_daily_deaths(country,days)
daily_recoveries_df = get_daily_recoveries(country,days)
daily_df = pd.concat([daily_cases_df,daily_deaths_df,daily_recoveries_df],axis=1).astype(int)

yesterday_cases_df = get_yesterday_cases(country)
yesterday_deaths_df = get_yesterday_deaths(country)
yesterday_recoveries_df = get_yesterday_recoveries(country)


st.title('This is my covid dashboard')

st.metric('Country',country)

st.metric('Total Cases', yesterday_cases_df)
st.metric('Total Deaths', yesterday_deaths_df)
st.metric('Total Recovered', yesterday_recoveries_df)
st.line
_chart(daily_df[data_type])

st.image("https://www.pexels.com/photo/landscape-nature-sky-man-6620743/")
st.video('https://www.youtube.com/watch?v=w5HvxsOo00E')


