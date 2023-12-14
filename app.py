import streamlit as st
from functions_button import st_button, load_css
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load your dataset
data = pd.read_csv("fatalities.csv")


# Create a Streamlit app
st.title("Dashboard Analisis Data \n Insiden Israel - Palestina")


st.sidebar.header("Informasi Data")
#display data 
def display_data():
    # displaying important information within sidebar
    # Number of events

    num_events = len(data)
    st.sidebar.write('Total Kejadian :',num_events)
    
    st.sidebar.image("pict.1.png", width=250)
    
    col1, col2 = st.sidebar.columns(2)
    col3, col4 = st.sidebar.columns(2)
    col5, col6 = st.sidebar.columns(2)
    citizenship_counts = data['citizenship'].value_counts()
    event_location_region_counts = data['event_location_region'].value_counts()
    hostilities_counts = data[data['took_part_in_the_hostilities'] == 'Yes']['citizenship'].value_counts()
    no_hostilities_counts = data[data['took_part_in_the_hostilities'] == 'No']['citizenship'].value_counts()
    weapons_used = data['ammunition'].value_counts()

    with col1:
        st.subheader("Lokasi Insiden")
        st.write(event_location_region_counts)
    with col2:
        st.subheader('Tanpa Perlawanan')
        st.write(no_hostilities_counts)
    with col3:
        st.subheader("Dengan Perlawanan")
        st.write(hostilities_counts)
    with col4:
        st.subheader("Kewarganegaraan")
        st.write(citizenship_counts)
    with col5:
        st.subheader("Amunisi")
        st.write(weapons_used)
    with col6:
        st.subheader("  ")

    
    

#=======================================================================================
    # Show a sample of the data
    st.header("Sample Data")
    st.write(data.head())

    # Data analysis section
    st.header("Analisis Data")


    col1,col2 = st.columns(2)

    with col1:
        # Group data by 'citizenship' and count incidents
        citizenship_counts = data['citizenship'].value_counts()
        st.subheader(" Berdasarkan Warga Negara")
        st.bar_chart(citizenship_counts,color='#228B22')
    with col2:
        # Group data by 'gender' and visualize
        gender_counts = data['gender'].value_counts()
        st.subheader(" Berdasarkan Gender")
        st.bar_chart(gender_counts,color='#FF8C00')


    col1,col2 = st.columns(2)

    with col1:
        # Calculate summary statistics for 'age'
        st.subheader("Statistik Usia")
        st.write(data['age'].describe())
    with col2:
        # Group data by 'event_location_region' and count incidents
        region_counts = data['event_location_region'].value_counts()
        st.subheader("Insiden Berdasarkan Negara")
        st.bar_chart(region_counts,color="#1E90FF")


    col1,col2 = st.columns(2)
    with col1:
        # Count unique values of 'place_of_residence' within each region
        st.subheader("Wilayah Tempat Tinggal Berdasarkan Negara ")
        unique_places_by_region = data.groupby('event_location_region')['place_of_residence'].nunique()
        st.write(unique_places_by_region)
    with col2:
        # Calculate average age by 'event_location_region'
        avg_age_by_region = data.groupby('event_location_region')['age'].mean()
        st.subheader("Rata-rata Usia Menurut Tiap Wilayah")
        st.write(avg_age_by_region)

    # Visualize the 3 top types of injuries using Matplotlib
    st.subheader("Presentase Jenis Luka")
    injury_counts = data['type_of_injury'].value_counts()
    #injury_counts = injury_counts[injury_counts > 5]
    top_3_counts = injury_counts.nlargest(3)
    top_3_labels = top_3_counts.index.to_list()
    fig, ax = plt.subplots()
    ax.pie(top_3_counts, labels=top_3_labels, autopct='%1.1f%%')
    ax.set_aspect('equal')
    st.pyplot(fig)
    

    # Data filtering example: Incidents in a specific region with specific characteristics
    region = 'West Bank'  
    filtered_data = data[(data['event_location_region'] == region) & (data['type_of_injury'] == 'gunfire')]
    st.subheader(f"Insiden di {region} Menurut Jenis Luka Tembakan")
    st.write(filtered_data)

    col1,col2 = st.columns(2)
    with col1:
        # Combining grouping and filtering(example: average  age  of males and females from a specific nationality  involved in specific injuries)
        avg_age = data[(data['citizenship'] == 'Palestinian') & (data['type_of_injury'] == 'stones throwing')].groupby('gender')[
        'age'].mean()
        st.subheader("Rata-Rata Usia Orang Yang Melempar Batu")
        st.write(avg_age)
    with col2: 
        # filtering with multiple conditions
        result = data[(data['citizenship'] == 'Palestinian') & (data['gender'] == 'F') & (data['type_of_injury'] == 'gunfire')][
        ['citizenship', 'gender', 'type_of_injury']]
        st.subheader("Jenis Luka Menurut Gender dan Kewarganegaraan")
        st.write(result)

    
    # Time-based analysis (events at specific times)
    data['date_of_event'] = pd.to_datetime(data['date_of_event'])
    data['year'] = data['date_of_event'].dt.year
    data['month'] = data['date_of_event'].dt.month_name()  # Format month as month name
    time_events = data.groupby(['year', 'month']).size().reset_index(name='incident_count')
    time_events['year_month'] = time_events['month'] + ' ' + time_events['year'].astype(str)
    st.subheader('Insiden Berdasarkan Waktu')
    st.line_chart(time_events.set_index('year_month')['incident_count'])

    # Calculate average age for female (F) citizens
    female_age = pd.pivot_table(data[data['gender'] == 'F'], values='age', index=['citizenship'], aggfunc='mean')
    st.subheader('Rata-rata Usia Korban Wanita')
    st.bar_chart(female_age,color='#228B22')

    # Calculate average age for male (M) citizens
    male_age = pd.pivot_table(data[data['gender'] == 'M'], values='age', index=['citizenship'], aggfunc='mean')
    st.subheader('Rata-rata Usia Korban Pria')
    st.bar_chart(male_age,color='#FF8C00')




#show your data 
display_data()
load_css()
icon_size = 20

# Footer
st_button('whatsapp', 'https://www.instagram.com/cak_jar/', 'More Information', icon_size)
st.sidebar.text("Created by Safjar")



