import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

day_df_cleaned = day_df.drop(columns=['instant'])
hour_df_cleaned = hour_df.drop(columns=['instant'])

st.title('Dashboard Analisis Data Bike Sharing')

st.header('Data Overview')
if st.checkbox('Show Day Dataset'):
    st.write(day_df)

if st.checkbox('Show Hour Dataset'):
    st.write(hour_df)

# 1. Impact of Weather on Total Bike Rentals
st.header('Impact of Weather on Bike Rentals')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='weathersit', y='cnt', data=day_df, ax=ax)
ax.set_title('Impact of Weather on Total Bike Rentals (Day)')
ax.set_xlabel('Weather Situation')
ax.set_ylabel('Total Rentals')
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(['Clear/Few Clouds', 'Mist/Cloudy', 'Light Snow/Rain', 'Heavy Rain/Snow'])
st.pyplot(fig)

# 2. Seasonal Patterns in Bike Rentals
st.header('Seasonal Patterns in Bike Rentals')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.lineplot(x='mnth', y='cnt', hue='season', style='season', markers=True, dashes=False, data=day_df_cleaned, palette='tab10', ax=ax2)
ax2.set_title('Seasonal Patterns in Bike Rentals')
ax2.set_xlabel('Month')
ax2.set_ylabel('Total Rentals')
ax2.set_xticks(range(1, 13))
ax2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax2.legend(title='Season', loc='upper left', labels=['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(fig2)

# 3. Bike Rentals on Working Day vs Weekend
st.header('Bike Rentals Distribution on Working Day vs Weekend')
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='workingday', y='cnt', data=day_df_cleaned, ax=ax3)
ax3.set_title('Bike Rentals Distribution on Working Day vs Weekend')
ax3.set_xlabel('Working Day (1: Hari Kerja, 0: Akhir Pekan)')
ax3.set_ylabel('Total Rentals')
ax3.set_xticks([0, 1])
ax3.set_xticklabels(['Akhir Pekan', 'Hari Kerja'])
st.pyplot(fig3)