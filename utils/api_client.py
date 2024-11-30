"""API client utilities for fetching environmental data."""
import requests
from datetime import datetime, timedelta
import random
from config import OPENAQ_API_URL, DEFAULT_LOCATION

class APIClient:
    @staticmethod
    def fetch_air_quality():
        """Fetch real air quality data from OpenAQ API."""
        params = {
            'city': DEFAULT_LOCATION['city'],
            'limit': 100,
            'parameter': ['pm25', 'no2', 'so2', 'co']
        }
        
        try:
            response = requests.get(OPENAQ_API_URL, params=params)
            if response.status_code == 200:
                return response.json()['results']
            return None
        except Exception as e:
            print(f"Error fetching air quality data: {e}")
            return None

    @staticmethod
    def simulate_water_quality():
        """Simulate water quality data."""
        return {
            'pH': round(random.uniform(6.0, 9.0), 2),
            'turbidity': round(random.uniform(0, 10), 2),
            'temperature': round(random.uniform(15, 30), 2),
            'timestamp': datetime.now().isoformat()
        }

    @staticmethod
    def get_historical_data(days=7):
        """Generate historical data for charts."""
        data = []
        for i in range(days):
            date = datetime.now() - timedelta(days=i)
            data.append({
                'date': date,
                'pm25': random.uniform(10, 150),
                'no2': random.uniform(20, 200),
                'ph': random.uniform(6.5, 8.5)
            })
        return data