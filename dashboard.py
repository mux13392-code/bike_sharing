import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# =========================
# Custom Theme
# =========================
st.set_page_config(
    page_title="🚲 Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #1f77b4;
    }
    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# Load Data
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv('day.csv')
    df['dteday'] = pd.to_datetime(df['dteday'])

    weather_map = {
        1: 'Clear',
        2: 'Cloudy',
        3: 'Drizzling',
        4: 'Heavy Rain'
    }
    df['weather_label'] = df['weathersit'].map(weather_map)

    df['casual_ratio'] = df['casual'] / df['cnt']
    df['registered_ratio'] = df['registered'] / df['cnt']

    df['month'] = df['dteday'].dt.strftime('%Y-%m')
    df['day_of_week'] = df['dteday'].dt.day_name()
    
    # Season mapping
    season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    df['season_label'] = df['season'].map(season_map)
    
    return df


day_df = load_data()

# =========================
# Sidebar Filter
# =========================
st.sidebar.header("🛠️ Filter Dashboard")
st.sidebar.markdown("---")

# Date Range Filter
date_range = st.sidebar.date_input(
    "Rentang Tanggal",
    value=(day_df['dteday'].min(), day_df['dteday'].max()),
    min_value=day_df['dteday'].min(),
    max_value=day_df['dteday'].max()
)

# Weather Filter
selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca",
    options=day_df['weather_label'].unique(),
)

# Season Filter
selected_season = st.sidebar.multiselect(
    "Pilih Musim",
    options=day_df['season_label'].unique(),
)

# Year Filter
selected_year = st.sidebar.multiselect(
    "Pilih Tahun",
    options=sorted(day_df['yr'].unique()),
    format_func=lambda x: "2011" if x == 0 else "2012"
)

# Apply Filters
filtered_df = day_df[
    (day_df['weather_label'].isin(selected_weather)) &
    (day_df['season_label'].isin(selected_season)) &
    (day_df['yr'].isin(selected_year))
]

if len(date_range) == 2:
    filtered_df = filtered_df[
        (filtered_df['dteday'] >= pd.to_datetime(date_range[0])) &
        (filtered_df['dteday'] <= pd.to_datetime(date_range[1]))
    ]

# =========================
# Header
# =========================
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Dashboard interaktif untuk analisis data penyewaan sepeda berdasarkan kondisi cuaca dan tipe pengguna (2011–2012).")
st.markdown("Pilih opsi untuk melihat tren penyewaan sepeda!")
# =========================
# KPI Metrics
# =========================

# =========================
# Tabs for Navigation
# =========================
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🌤️ Cuaca & Musim", "📈 Tren Waktu", "🔍 Analisis Lanjutan"])

# =========================
# Tab 1: Overview
# =========================
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Rata-rata Penyewaan Berdasarkan Kondisi Cuaca")
        weather_avg = filtered_df.groupby('weather_label')['cnt'].mean().reset_index()
        
        fig = px.bar(
            weather_avg, 
            x='weather_label', 
            y='cnt',
            color='weather_label',
            color_discrete_sequence=px.colors.qualitative.Set2,
            text_auto='.0f'
        )
        fig.update_layout(xaxis_title='Kondisi Cuaca', yaxis_title='Rata-rata Penyewaan')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Distribusi Tipe Pengguna")
        user_type = pd.DataFrame({
            'Tipe': ['Casual', 'Registered'],
            'Jumlah': [filtered_df['casual'].sum(), filtered_df['registered'].sum()]
        })
        
        fig = px.pie(
            user_type, 
            values='Jumlah', 
            names='Tipe',
            color_discrete_sequence=['#FF6B6B', '#4ECDC4'],
            hole=0.4
        )
        st.plotly_chart(fig, use_container_width=True)

# =========================
# Tab 2: Cuaca & Musim
# =========================
with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Penyewaan Berdasarkan Musim")
        season_avg = filtered_df.groupby('season_label')['cnt'].mean().reset_index()
        
        fig = px.bar(
            season_avg,
            x='season_label',
            y='cnt',
            color='season_label',
            color_discrete_sequence=px.colors.qualitative.Pastel,
            text_auto='.0f'
        )
        fig.update_layout(xaxis_title='Musim', yaxis_title='Rata-rata Penyewaan')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Hubungan Suhu vs Penyewaan")
        fig = px.scatter(
            filtered_df,
            x='temp',
            y='cnt',
            color='season_label',
            size='cnt',
            color_discrete_sequence=px.colors.qualitative.Set1,
            trendline="ols"
        )
        fig.update_layout(xaxis_title='Suhu (Normalized)', yaxis_title='Jumlah Penyewaan')
        st.plotly_chart(fig, use_container_width=True)

# =========================
# Tab 3: Tren Waktu
# =========================
with tab3:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Tren Penyewaan Bulanan")
        monthly_trend = filtered_df.groupby('month')['cnt'].mean().reset_index()
        
        fig = px.line(
            monthly_trend,
            x='month',
            y='cnt',
            markers=True,
            line_shape='spline'
        )
        fig.update_traces(line_color='#1f77b4', line_width=3)
        fig.update_layout(xaxis_title='Bulan', yaxis_title='Rata-rata Penyewaan')
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Proporsi Casual vs Registered")
        monthly_ratio = filtered_df.groupby('month').agg({
            'casual_ratio': 'mean',
            'registered_ratio': 'mean'
        }).reset_index()
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=monthly_ratio['month'], y=monthly_ratio['casual_ratio'], 
                                 name='Casual', line=dict(color='#FF6B6B')), secondary_y=False)
        fig.add_trace(go.Scatter(x=monthly_ratio['month'], y=monthly_ratio['registered_ratio'], 
                                 name='Registered', line=dict(color='#4ECDC4')), secondary_y=True)
        fig.update_layout(xaxis_title='Bulan', yaxis_title='Proporsi Casual', yaxis2_title='Proporsi Registered')
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

# =========================
# Tab 4: Analisis Lanjutan
# =========================
with tab4:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Correlation Matrix")
        corr = filtered_df[['cnt', 'temp', 'atemp', 'hum', 'windspeed']].corr()
        
        fig = px.imshow(
            corr,
            text_auto='.2f',
            color_continuous_scale='RdBu_r',
            aspect='auto'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Kategori Penyewaan")
        filtered_df = filtered_df.copy()
        filtered_df['rental_category'] = pd.cut(
            filtered_df['cnt'],
            bins=[0, 2000, 5000, 9000],
            labels=['Low', 'Medium', 'High']
        )
        
        category_counts = filtered_df['rental_category'].value_counts().reset_index()
        category_counts.columns = ['Kategori', 'Jumlah']
        
        fig = px.bar(
            category_counts,
            x='Kategori',
            y='Jumlah',
            color='Kategori',
            color_discrete_sequence=px.colors.qualitative.Set3,
            text='Jumlah'
        )
        st.plotly_chart(fig, use_container_width=True)

# =========================
# Data Table
# =========================
with st.expander("📋 Lihat Data Mentah"):
    st.dataframe(filtered_df.head(50), use_container_width=True)
    st.caption(f"Menampilkan 50 dari {len(filtered_df)} baris data")

# =========================
# Footer
# =========================
st.markdown('---')
st.caption('🚲 Bike Sharing Dashboard | Data Analysis Project | Dibuat dengan Streamlit')