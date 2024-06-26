# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd

# Tautan unduhan langsung Google Drive
url = 'https://drive.google.com/uc?export=download&id=1DEAX6Zw46GyLzlC2XulkLdIQCpREdXRl'

# Membaca file CSV
day = pd.read_csv(url)

# Menampilkan data
day.head()

import pandas as pd

# Tautan unduhan langsung Google Drive
url = 'https://drive.google.com/uc?export=download&id=1NlvkobNiWLBTJkJZ0SC1bRhZhneNrinp'

# Membaca file CSV
hour = pd.read_csv(url)

# Menampilkan data
hour.head()



day.info()

day.describe()

print('data duplikat  : ', day.duplicated().sum())
print('data null      : ', day.isnull().sum())

hour.info()

hour.describe()

print('data duplikat  : ', hour.duplicated().sum())
print('data null      : ', hour.isnull().sum())



import pandas as pd
# there is no missing value and duplicate value in both dataset
# change dteday to datetime
day['dteday'] = pd.to_datetime(day['dteday'])
hour['dteday'] = pd.to_datetime(hour['dteday'])

#merename nama pada setiap kolom agar lebih jelas di baca

day = day.rename(columns={
    'instant': 'record_id',
    'dteday': 'date_day',
    'season': 'season_num',
    'yr': 'year',
    'mnth': 'month',
    'holiday': 'is_holiday',
    'weekday': 'day_of_week',
    'workingday': 'is_workingday',
    'weathersit': 'weather_condition',
    'temp': 'normalized_temp',
    'atemp': 'normalized_feeling_temp',
    'hum': 'normalized_humidity',
    'windspeed': 'normalized_windspeed',
    'casual': 'casual_users',
    'registered': 'registered_users',
    'cnt': 'total_users'
})

hour = hour.rename(columns={
    'instant': 'record_id',
    'dteday': 'date_day',
    'season': 'season_num',
    'yr': 'year',
    'mnth': 'month',
    'hr': 'hour',
    'holiday': 'is_holiday',
    'weekday': 'day_of_week',
    'workingday': 'is_workingday',
    'weathersit': 'weather_condition',
    'temp': 'normalized_temp',
    'atemp': 'normalized_feeling_temp',
    'hum': 'normalized_humidity',
    'windspeed': 'normalized_windspeed',
    'casual': 'casual_users',
    'registered': 'registered_users',
    'cnt': 'total_users'
})

# ubah season dari angka menjadi nama musim
day['season_num'] = day['season_num'].replace({1: 'springer', 2: 'summer', 3: 'fall', 4: 'winter'})
hour['season_num'] = hour['season_num'].replace({1: 'springer', 2: 'summer', 3: 'fall', 4: 'winter'})

# ubah tahun dari angka menjadi tahun
day['year'] = day['year'].replace({0: 2011, 1: 2012})
hour['year'] = hour['year'].replace({0: 2011, 1: 2012})

import pandas as pd
# ubah bulan dari angka menjadi nama bulan
day['month'] = day['month'].replace({1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'})
hour['month'] = hour['month'].replace({1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'})

# ubah hari dari angka menjadi nama hari
day['day_of_week'] = day['day_of_week'].replace({0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'})
hour['day_of_week'] = hour['day_of_week'].replace({0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'})

# ubah cuaca dari angka menjadi keterangan cuaca
day['weather_condition'] = day['weather_condition'].replace({1: 'Clear', 2: 'Mist', 3: 'Light Snow', 4: 'Heavy Rain'})
hour['weather_condition'] = hour['weather_condition'].replace({1: 'Clear', 2: 'Mist', 3: 'Light Snow', 4: 'Heavy Rain'})

# ubah hari kerja dari angka menjadi keterangan hari kerja
day['is_workingday'] = day['is_workingday'].replace({0: 'Holiday', 1: 'Working Day'})
hour['is_workingday'] = hour['is_workingday'].replace({0: 'Holiday', 1: 'Working Day'})

# ubah liburan dari angka menjadi keterangan liburan
day['is_holiday'] = day['is_holiday'].replace({0: 'Not Holiday', 1: 'Holiday'})
hour['is_holiday'] = hour['is_holiday'].replace({0: 'Not Holiday', 1: 'Holiday'})

# mengubah urutan bulan
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
day['month'] = pd.Categorical(day['month'], categories=month_order, ordered=True)
hour['month'] = pd.Categorical(hour['month'], categories=month_order, ordered=True)

# ubah cuaca dari angka menjadi keterangan cuaca
day['weather_condition'] = day['weather_condition'].replace({1: 'Clear', 2: 'Mist', 3: 'Light Snow', 4: 'Heavy Rain'})
hour['weather_condition'] = hour['weather_condition'].replace({1: 'Clear', 2: 'Mist', 3: 'Light Snow', 4: 'Heavy Rain'})

day.head()

hour.head()


import matplotlib.pyplot as plt
#membuat dataframe baru untuk agregasi data
monthly_counts = day.groupby('month')[['casual_users', 'registered_users']].sum().reset_index()

#membuat visualisasi data
plt.figure(figsize=(12, 6))
plt.plot(monthly_counts['month'], monthly_counts['casual_users'], label='Casual Users', marker='o')
plt.plot(monthly_counts['month'], monthly_counts['registered_users'], label='Registered Users', marker='o')
plt.xlabel('Month')
plt.ylabel('Number of Users')
plt.title('Monthly Trend of Bike Usage')
plt.legend()
plt.grid(True)

#menambahkan titik titik penjelas untuk setiap bulan
for i, month in enumerate(monthly_counts['month']):
    plt.annotate('.', (month, monthly_counts['casual_users'][i]), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate('.', (month, monthly_counts['registered_users'][i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()

#menampilkan tabel data
print(monthly_counts)


import matplotlib.pyplot as plt
# Membuat dataframe baru untuk agregasi data berdasarkan musim dan kondisi cuaca
seasonal_weather_counts = day.groupby(['season_num', 'weather_condition'])['total_users'].sum().reset_index()

# Membuat visualisasi data
plt.figure(figsize=(12, 6))
sns.barplot(x='season_num', y='total_users', hue='weather_condition', data=seasonal_weather_counts)
plt.xlabel('Season')
plt.ylabel('Total Number of Users')
plt.title('Impact of Season and Weather on Bike Usage')
plt.legend()
plt.grid(True)
plt.show()

# Menampilkan tabel data
print(seasonal_weather_counts)



import pandas as pd
import matplotlib.pyplot as plt
# Menghitung nilai Recency, Frequency, dan Monetary untuk setiap pengguna
# Karena dataset tidak memiliki informasi transaksi, kita akan menggunakan 'date_day' sebagai proxy untuk Recency,
# jumlah perjalanan sebagai proxy untuk Frequency, dan total pengguna sebagai proxy untuk Monetary.

# Mengambil tanggal terakhir dalam dataset
snapshot_date = day['date_day'].max() + pd.Timedelta(days=1)

# Menghitung RFM untuk pengguna casual
rfm_casual = day.groupby('record_id').agg({
    'date_day': lambda x: (snapshot_date - x.max()).days,  # Recency
    'casual_users': 'sum',  # Frequency
    'total_users': 'sum'  # Monetary
}).rename(columns={
    'date_day': 'Recency',
    'casual_users': 'Frequency',
    'total_users': 'Monetary'
})

# Menghitung RFM untuk pengguna registered
rfm_registered = day.groupby('record_id').agg({
    'date_day': lambda x: (snapshot_date - x.max()).days,  # Recency
    'registered_users': 'sum',  # Frequency
    'total_users': 'sum'  # Monetary
}).rename(columns={
    'date_day': 'Recency',
    'registered_users': 'Frequency',
    'total_users': 'Monetary'
})

# Menentukan skor RFM (1-4) berdasarkan quartile
# Semakin rendah skor Recency, semakin baik. Semakin tinggi skor Frequency dan Monetary, semakin baik.
for df in [rfm_casual, rfm_registered]:
    df['R_Quartile'] = pd.qcut(df['Recency'], q=4, labels=range(4, 0, -1))
    df['F_Quartile'] = pd.qcut(df['Frequency'], q=4, labels=range(1, 5))
    df['M_Quartile'] = pd.qcut(df['Monetary'], q=4, labels=range(1, 5))

# Menggabungkan skor RFM menjadi satu skor
rfm_casual['RFM_Score'] = rfm_casual['R_Quartile'].astype(str) + rfm_casual['F_Quartile'].astype(str) + rfm_casual['M_Quartile'].astype(str)
rfm_registered['RFM_Score'] = rfm_registered['R_Quartile'].astype(str) + rfm_registered['F_Quartile'].astype(str) + rfm_registered['M_Quartile'].astype(str)

# Membuat segmentasi pelanggan berdasarkan skor RFM
def segment_customer(df):
    if df['RFM_Score'] >= '444':
        return 'Champions'
    elif df['RFM_Score'] >= '333':
        return 'Loyal Customers'
    elif df['RFM_Score'] >= '222':
        return 'Potential Loyalists'
    elif df['RFM_Score'] >= '111':
        return 'New Customers'
    else:
        return 'At Risk'

rfm_casual['Segment'] = rfm_casual.apply(segment_customer, axis=1)
rfm_registered['Segment'] = rfm_registered.apply(segment_customer, axis=1)

# Visualisasi distribusi segmen pelanggan
plt.figure(figsize=(10, 6))
sns.countplot(x='Segment', data=rfm_casual, order=['Champions', 'Loyal Customers', 'Potential Loyalists', 'New Customers', 'At Risk'])
plt.title('Customer Segmentation for Casual Users')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='Segment', data=rfm_registered, order=['Champions', 'Loyal Customers', 'Potential Loyalists', 'New Customers', 'At Risk'])
plt.title('Customer Segmentation for Registered Users')
plt.xticks(rotation=45)
plt.show()

# Menampilkan tabel RFM dan segmentasi
print("RFM and Segmentation for Casual Users:")
print(rfm_casual.head())
print("\n")
print("RFM and Segmentation for Registered Users:")
print(rfm_registered.head())



import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import requests
from PIL import Image
from io import BytesIO
import streamlit as st

# Menambahkan logo
logo_url = 'https://drive.google.com/uc?export=download&id=19TQXDifG-3oj_2UH4_J97K0fsyo-5e_p'
response = requests.get(logo_url)
logo_img = Image.open(BytesIO(response.content))
st.sidebar.image(logo_img, use_column_width=True)


# URL unduhan langsung Google Drive
url = 'https://drive.google.com/uc?export=download&id=1iK0iM1KvdDS7O-IiV8xEgDvJZt_X5wss'

# Mengunduh gambar
response = requests.get(url)
response.raise_for_status()  # Memastikan permintaan berhasil

# Simpan gambar ke disk
image_path = 'downloaded_image.jpg'
with open(image_path, 'wb') as f:
    f.write(response.content)

# Judul Dashboard
st.title('Bike Sharing Web APP :bike:')

# Sidebar
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Home','Data Overview', 'Overal Metrics','EDA', 'RFM Analysis'])


# Halaman Home
if page == 'Home':
    st.header('Welcome to the Bike Sharing Dashboard!')
    image = Image.open(image_path)  
    img_resized = image.resize((150, 50))
    st.image(img_resized, caption='Bike Sharing', use_column_width=True)
    st.write('This dashboard provides insights into bike sharing usage patterns based on various factors such as season, weather, time of day, and user type.')

# Halaman Data Overview
elif page == 'Data Overview':
    st.header('Data Overview')
    st.subheader('Dataset Day')
    st.write(day.head())
    st.subheader('Dataset Hour')
    st.write(hour.head())

# Halaman EDA
elif page == 'EDA':
    st.header('Exploratory Data Analysis')

    # Visualisasi 1: Tren Penggunaan Sepeda Bulanan
    st.subheader('Monthly Trend of Bike Usage')
    monthly_counts = day.groupby('month')[['casual_users', 'registered_users']].sum().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(monthly_counts['month'], monthly_counts['casual_users'], label='Casual Users', marker='o')
    ax.plot(monthly_counts['month'], monthly_counts['registered_users'], label='Registered Users', marker='o')
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Users')
    ax.set_title('Monthly Trend of Bike Usage')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Visualisasi 2: Dampak Musim dan Cuaca terhadap Penggunaan Sepeda
    st.subheader('Impact of Season and Weather on Bike Usage')
    seasonal_weather_counts = day.groupby(['season_num', 'weather_condition'])['total_users'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='season_num', y='total_users', hue='weather_condition', data=seasonal_weather_counts, ax=ax)
    ax.set_xlabel('Season')
    ax.set_ylabel('Total Number of Users')
    ax.set_title('Impact of Season and Weather on Bike Usage')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Visualisasi Tambahan: Distribusi Pengguna Sepeda per Jam
    st.subheader('Distribution of Bike Users per Hour')
    hourly_counts = hour.groupby('hour')['total_users'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='hour', y='total_users', data=hourly_counts, ax=ax)
    ax.set_xlabel('Hour')
    ax.set_ylabel('Total Number of Users')
    ax.set_title('Distribution of Bike Users per Hour')
    ax.grid(True)
    st.pyplot(fig)

# Halaman RFM Analysis
elif page == 'RFM Analysis':
    st.header('RFM Analysis')



    # Visualisasi: Distribusi Segmen Pelanggan
    st.subheader('Customer Segmentation')
    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    sns.countplot(x='Segment', data=rfm_casual, order=['Champions', 'Loyal Customers', 'Potential Loyalists', 'New Customers', 'At Risk'], ax=ax[0])
    ax[0].set_title('Customer Segmentation for Casual Users')
    ax[0].tick_params(axis='x', rotation=45)
    sns.countplot(x='Segment', data=rfm_registered, order=['Champions', 'Loyal Customers', 'Potential Loyalists', 'New Customers', 'At Risk'], ax=ax[1])
    ax[1].set_title('Customer Segmentation for Registered Users')
    ax[1].tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    # Widget Tambahan: Filter Data berdasarkan Segmen
    segment_filter = st.selectbox('Select Customer Segment', ['All', 'Champions', 'Loyal Customers', 'Potential Loyalists', 'New Customers', 'At Risk'])
    if segment_filter != 'All':
        st.write(rfm_casual[rfm_casual['Segment'] == segment_filter])
        st.write(rfm_registered[rfm_registered['Segment'] == segment_filter])
    
    # Widget Tambahan: Slider untuk Memfilter Rentang Recency
    st.subheader('Filter by Recency')
    min_recency, max_recency = st.slider('Select Recency Range', 0, int(rfm_casual['Recency'].max()), (0, int(rfm_casual['Recency'].max())))
    filtered_casual = rfm_casual[(rfm_casual['Recency'] >= min_recency) & (rfm_casual['Recency'] <= max_recency)]
    filtered_registered = rfm_registered[(rfm_registered['Recency'] >= min_recency) & (rfm_registered['Recency'] <= max_recency)]
    st.write('Filtered Casual Users:')
    st.write(filtered_casual)
    st.write('Filtered Registered Users:')
    st.write(filtered_registered)

    # Widget Tambahan: Multiselect untuk Memilih Beberapa Musim
    st.subheader('Filter by Season')
    selected_seasons = st.multiselect('Select Seasons', day['season_num'].unique())
    if selected_seasons:
        filtered_day = day[day['season_num'].isin(selected_seasons)]
        st.write(filtered_day)

# Halaman Overal Metrics
elif page == 'Overal Metrics':
    st.header('Overal Metrics :bar_chart:')

    # Metrik 1: Total Pengguna Harian Rata-rata
    avg_daily_users = day['total_users'].mean()
    st.subheader('Average Daily Users')
    st.metric(label="", value=f"{avg_daily_users:.2f}", delta=None)

    # Metrik 2: Persentase Pengguna Casual vs Registered
    total_casual = day['casual_users'].sum()
    total_registered = day['registered_users'].sum()
    casual_percentage = (total_casual / (total_casual + total_registered)) * 100
    registered_percentage = (total_registered / (total_casual + total_registered)) * 100
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Casual Users Percentage')
        st.metric(label="", value=f"{casual_percentage:.2f}%", delta=None)
    with col2:
        st.subheader('Registered Users Percentage')
        st.metric(label="", value=f"{registered_percentage:.2f}%", delta=None)

    # Metrik 3: Pengaruh Cuaca terhadap Penggunaan Sepeda
    weather_impact = day.groupby('weather_condition')['total_users'].mean().sort_values(ascending=False)
    st.subheader('Weather Impact on Bike Usage')
    st.bar_chart(weather_impact)

    # Tombol untuk menampilkan data mentah
    if st.button('Show Raw Data'):
        st.write(day)




st.caption('Copyright (C) Muhammad Rayhan Aidy Abshar - Project Dicoding . 2024')