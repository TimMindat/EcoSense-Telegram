"""Configuration settings for the EcoSense Telegram bot."""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv('BOT_TOKEN')  # Remove default value to ensure token is properly loaded
OPENAQ_API_URL = "https://api.openaq.org/v2/measurements"

# Default location (Cairo)
DEFAULT_LOCATION = {
    'city': 'Cairo',
    'coordinates': {'latitude': 30.0444, 'longitude': 31.2357}
}

# Thresholds for air quality parameters
AQI_THRESHOLDS = {
    'PM2.5': {'good': 12, 'moderate': 35.4, 'unhealthy': 55.4},
    'NO2': {'good': 53, 'moderate': 100, 'unhealthy': 360},
    'SO2': {'good': 35, 'moderate': 75, 'unhealthy': 185},
    'CO': {'good': 4.4, 'moderate': 9.4, 'unhealthy': 12.4}
}

# Water quality thresholds
WATER_THRESHOLDS = {
    'pH': {'min': 6.5, 'max': 8.5},
    'turbidity': {'max': 5},  # NTU
    'temperature': {'min': 10, 'max': 25}  # Celsius
}

# Command descriptions
COMMAND_DESCRIPTIONS = {
    'start': 'Get started with EcoSense Bot',
    'air_quality': 'Get real-time air quality data',
    'water_quality': 'Get current water quality data',
    'charts': 'View environmental data charts',
    'settings': 'Configure your notification preferences',
    'help': 'Show all available commands'
}