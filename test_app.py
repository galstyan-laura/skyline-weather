import pytest
from unittest.mock import patch
import streamlit as st
from app import get_weather

@patch('requests.get')
@pytest.mark.parametrize("city_name", ["Yerevan", "Paris", "Tokyo", "New York"])
def test_get_weather_multiple_cities(mock_get, city_name):
    st.cache_data.clear()
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "name": city_name,
        "main": {"temp": 20.0, "feels_like": 19.5, "humidity": 50, "pressure": 1015},
        "wind": {"speed": 2.0, "deg": 180},
        "clouds": {"all": 10},
        "sys": {"country": "AM"},
        "coord": {"lat": 40.0, "lon": 44.0}
    }

    result = get_weather(city_name)
    assert result is not None
    assert result["name"] == city_name