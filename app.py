import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Skyline Weather Portal",
    page_icon="🌍",
    layout="wide"
)

# CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #080c14;
        color: #f1f5f9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0d1322;
        border-right: 1px solid rgba(255, 255, 255, 0.06);
    }

    /* Header Panel */
    .skyline-header {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #334155;
    margin-bottom: 20px;
}

    /* Weather Cards */
    .weather-card {
        background: rgba(17, 24, 39, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(12px);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card-title {
        font-size: 0.85rem;
        font-weight: 700;
        color: #94a3b8;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 12px;
    }
    .card-main-value {
        font-size: 3.2rem;
        font-weight: 700;
        color: #f8fafc;
        line-height: 1.1;
        margin-bottom: 8px;
    }
    .card-subtext {
        font-size: 1.1rem;
        color: #e2e8f0;
        font-weight: 500;
        margin-bottom: 24px;
    }
    .card-footer-info {
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        padding-top: 16px;
        display: flex;
        justify-content: space-between;
        font-size: 0.95rem;
        color: #94a3b8;
    }

    /* 5-Day Forecast Row Style */
    .forecast-row {
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 12px 18px;
        margin-bottom: 8px;
        display: grid;
        grid-template-columns: 140px 60px 80px 1fr 60px;
        align-items: center;
        backdrop-filter: blur(6px);
    }
    .forecast-row:hover {
        border-color: rgba(56, 189, 248, 0.3);
        background: rgba(15, 23, 42, 0.8);
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(15, 23, 42, 0.5);
        border-radius: 6px;
        color: #94a3b8;
        padding: 8px 18px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(56, 189, 248, 0.15) !important;
        color: #38bdf8 !important;
        border-color: rgba(56, 189, 248, 0.4) !important;
    }
    </style>
""", unsafe_allow_html=True)

API_KEY = "2981307479be85feb0c13d9267a51aa0"

# Sidebar Controls
with st.sidebar:
    st.markdown("### 🌍 Location Setup")
    city = st.text_input("📍 Location Search", value="Yerevan")
    st.markdown("---")
    st.info("💡 **Ventura Engine:** Real-time atmospheric mapping simulation.")

# API Helper Functions
@st.cache_data(ttl=300)
def get_weather(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    return res.json() if res.status_code == 200 else None

@st.cache_data(ttl=300)
def fetch_forecast(city_name):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    return res.json() if res.status_code == 200 else None

# Header Panel
st.markdown("""
    <div class="skyline-header">
        <h1 style="margin:0; font-size: 1.8rem; color: #f8fafc;">🏙️ Skyline Weather Portal</h1>
        <p style="margin:6px 0 0 0; color: #94a3b8; font-size: 0.95rem;">Advanced meteorological intelligence, live telemetry, and atmospheric forecasting.</p>
    </div>
""", unsafe_allow_html=True)

if city:
    data = get_weather(city)

    if data:
        lat, lon = data['coord']['lat'], data['coord']['lon']
        forecast_data = fetch_forecast(city)
        
        # Tabs layout
        tab1, tab2, tab3 = st.tabs(["🗺️ Live Map & Radar", "📅 5-Day Trend & Hourly Conditions", "🍃 Atmospheric Insights & Telemetry"])

        with tab1:
            st.subheader(f"📍 Region: {data['name']}, {data['sys'].get('country', '')}")
            
            # 4 KPI Mini Cards
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown(f'''<div class="weather-card" style="padding:18px;"><div class="card-title">Temperature</div><div class="card-main-value" style="font-size:2rem; color:#38bdf8;">{data["main"]["temp"]}°C</div><div class="card-subtext" style="font-size:0.9rem; margin-bottom:0;">Feels: {data["main"]["feels_like"]}°C</div></div>''', unsafe_allow_html=True)
            with col2:
                st.markdown(f'''<div class="weather-card" style="padding:18px;"><div class="card-title">Humidity</div><div class="card-main-value" style="font-size:2rem; color:#38bdf8;">{data["main"]["humidity"]}%</div><div class="card-subtext" style="font-size:0.9rem; margin-bottom:0;">Pressure: {data["main"]["pressure"]} hPa</div></div>''', unsafe_allow_html=True)
            with col3:
                st.markdown(f'''<div class="weather-card" style="padding:18px;"><div class="card-title">Wind Vector</div><div class="card-main-value" style="font-size:2rem; color:#38bdf8;">{data["wind"]["speed"]} m/s</div><div class="card-subtext" style="font-size:0.9rem; margin-bottom:0;">Direction: {data["wind"].get("deg", 0)}°</div></div>''', unsafe_allow_html=True)
            with col4:
                st.markdown(f'''<div class="weather-card" style="padding:18px;"><div class="card-title">Cloud Cover</div><div class="card-main-value" style="font-size:2rem; color:#38bdf8;">{data["clouds"]["all"]}%</div><div class="card-subtext" style="font-size:0.9rem; margin-bottom:0;">Altitude visibility</div></div>''', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            
            map_df = pd.DataFrame({
                'City': [data['name']],
                'Lat': [lat],
                'Lon': [lon],
                'Temp (°C)': [data['main']['temp']]
            })
            
            fig_map = px.scatter_geo(
                map_df, lat="Lat", lon="Lon", text="City",
                color="Temp (°C)", color_continuous_scale="Viridis",
                projection="natural earth", height=380
            )
            fig_map.update_geos(
                bgcolor="rgba(0,0,0,0)",
                landcolor="#1e293b",
                showocean=True, oceancolor="#0f172a",
                showcountries=True, countrycolor="#334155"
            )
            fig_map.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=0, r=0, t=0, b=0)
            )
            st.plotly_chart(fig_map, width='stretch')

        with tab2:
            st.subheader("🌤️ 5-Day Forecast & Interactive Hourly Conditions")
            
            if forecast_data and 'list' in forecast_data:
                forecast_list = forecast_data['list']
                daily_data = {}
                
                for item in forecast_list:
                    dt_txt = item['dt_txt']
                    date_str = dt_txt.split(' ')[0]
                    time_str = dt_txt.split(' ')[1][:5]
                    temp = item['main']['temp']
                    weather_desc = item['weather'][0]['description'].title()
                    
                    if date_str not in daily_data:
                        daily_data[date_str] = {'temps': [], 'hourly': [], 'desc': weather_desc}
                    
                    daily_data[date_str]['temps'].append(temp)
                    daily_data[date_str]['hourly'].append({'time': time_str, 'temp': temp})
                
                available_dates = list(daily_data.keys())[:5]
                formatted_dates_map = {}
                for d in available_dates:
                    dt_obj = datetime.strptime(d, "%Y-%m-%d")
                    formatted_dates_map[dt_obj.strftime("%A, %b %d, %Y")] = d
                
                # Selectbox without any label text above it
                selected_label = st.selectbox("", list(formatted_dates_map.keys()), label_visibility="collapsed")
                selected_date_str = formatted_dates_map[selected_label]
                
                selected_info = daily_data[selected_date_str]
                hourly_df = pd.DataFrame(selected_info['hourly'])
                
                fig_hourly = px.line(
                    hourly_df, x='time', y='temp',
                    markers=True,
                    labels={'time': 'Ժամ', 'temp': 'Ջերմաստիճան (°C)'},
                    height=280
                )
                fig_hourly.update_traces(
                    line_color='#fbbf24', 
                    line_width=3, 
                    marker=dict(size=9, color='#ffffff', line=dict(width=2, color='#fbbf24')),
                    hovertemplate='<b>Ժամը՝ %{x}</b><br>Ջերմաստիճան՝ %{y:.1f}°C<extra></extra>'
                )
                fig_hourly.update_layout(
                    paper_bgcolor="rgba(17,24,39,0.85)",
                    plot_bgcolor="rgba(15,23,42,0.8)",
                    font=dict(color="#f1f5f9"),
                    margin=dict(l=20, r=20, t=20, b=20),
                    xaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.06)", title=""),
                    yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.06)", title="")
                )
                st.plotly_chart(fig_hourly, width='stretch')
                
                st.markdown("---")
                st.markdown("### 📋 5-Day Overview List")
                
                for date_str, info in list(daily_data.items())[:5]:
                    max_t = round(max(info['temps']))
                    min_t = round(min(info['temps']))
                    dt_obj = datetime.strptime(date_str, "%Y-%m-%d")
                    day_name = dt_obj.strftime("%a")
                    full_date = dt_obj.strftime("%b %d")
                    
                    st.markdown(f"""
                        <div class="forecast-row">
                            <span style="font-weight: 600; color: #f8fafc;">{day_name}, {full_date}</span>
                            <span style="font-size: 1.1rem; color: #94a3b8;">🌤️</span>
                            <span style="font-weight: 600; color: #94a3b8; text-align: right;">{min_t}°</span>
                            <div style="background: rgba(255,255,255,0.1); border-radius: 4px; height: 6px; width: 100%; position: relative;">
                                <div style="background: linear-gradient(90deg, #38bdf8, #fbbf24); border-radius: 4px; height: 6px; width: 75%; margin-left: 15%;"></div>
                            </div>
                            <span style="font-weight: 700; color: #f8fafc; text-align: right;">{max_t}°</span>
                        </div>
                    """, unsafe_allow_html=True)

        with tab3:
            st.subheader("📊 Atmospheric Insights & Telemetry")
            st.markdown("<br>", unsafe_allow_html=True)
            
            temp_val = data["main"]["temp"]
            feels_val = data["main"]["feels_like"]
            max_val = data["main"]["temp_max"]
            wind_spd = data["wind"]["speed"]
            
            diff_avg = round(temp_val - 21, 1)
            diff_sign = "+" if diff_avg >= 0 else ""
            feel_desc = "Wind is making it feel cooler." if feels_val < temp_val else "Humidity is making it feel warmer."
            
            col_a, col_b, col_c = st.columns(3)
            
            with col_a:
                st.markdown(f'''
                    <div class="weather-card">
                        <div>
                            <div class="card-title">📈 Averages</div>
                            <div class="card-main-value">{diff_sign}{diff_avg}°</div>
                            <div class="card-subtext">above average daily high</div>
                        </div>
                        <div class="card-footer-info">
                            <span>Today</span>
                            <span style="color:#f8fafc; font-weight:600;">H:{round(max_val)}°</span>
                        </div>
                        <div class="card-footer-info" style="border-top:none; padding-top:4px;">
                            <span>Average</span>
                            <span style="color:#f8fafc; font-weight:600;">H:24°</span>
                        </div>
                    </div>
                ''', unsafe_allow_html=True)
                
            with col_b:
                st.markdown(f'''
                    <div class="weather-card">
                        <div>
                            <div class="card-title">🌡️ Feels Like</div>
                            <div class="card-main-value">{round(feels_val)}°</div>
                            <div class="card-subtext">{feel_desc}</div>
                        </div>
                        <div class="card-footer-info">
                            <span>Actual Temp</span>
                            <span style="color:#f8fafc; font-weight:600;">{round(temp_val)}°C</span>
                        </div>
                    </div>
                ''', unsafe_allow_html=True)
                
            with col_c:
                st.markdown(f'''
                    <div class="weather-card">
                        <div>
                            <div class="card-title">💨 Wind Telemetry</div>
                            <div class="card-main-value">{wind_spd} <span style="font-size:1.5rem">m/s</span></div>
                            <div class="card-subtext">Vector direction: {data["wind"].get("deg", 0)}°</div>
                        </div>
                        <div class="card-footer-info">
                            <span>Atmosphere</span>
                            <span style="color:#38bdf8; font-weight:600;">Stable</span>
                        </div>
                    </div>
                ''', unsafe_allow_html=True)
                
    else:
        st.error(f"⚠️ Could not locate region '{city}'. Please check the spelling.")