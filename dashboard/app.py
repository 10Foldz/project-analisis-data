import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

st.title('Dashboard Analisis Data Bike Sharing')

st.header('Data Overview')
if st.checkbox('Show Day Dataset'):
    st.write(day_df)

if st.checkbox('Show Hour Dataset'):
    st.write(hour_df)

st.header('Impact of Weather on Bike Rentals')
weather_data = day_df[['weathersit', 'cnt']]
weather_summary = weather_data.groupby('weathersit').mean().reset_index()

fig, ax = plt.subplots()
sns.boxplot(x='weathersit', y='cnt', data=day_df, ax=ax)
ax.set_title('Impact of Weather on Total Bike Rentals (Day)')
ax.set_xlabel('Weather Situation')
ax.set_ylabel('Total Rentals')
ax.set_xticklabels(['Clear/Few Clouds', 'Mist/Cloudy', 'Light Snow/Rain', 'Heavy Rain/Snow'])

st.pyplot(fig)

st.header('Seasonal Patterns in Bike Rentals')
fig2, ax2 = plt.subplots()
sns.lineplot(x='mnth', y='cnt', hue='season', data=day_df, ax=ax2)
ax2.set_title('Seasonal Bike Rental Patterns (Day)')
ax2.set_xlabel('Month')
ax2.set_ylabel('Total Rentals')
ax2.set_xticks(range(1, 13))
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax2.legend(title='Season', loc='upper left', labels=['Spring', 'Summer', 'Fall', 'Winter'])

st.pyplot(fig2)