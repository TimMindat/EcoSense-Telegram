"""Utilities for generating charts and visualizations."""
import matplotlib.pyplot as plt
import io
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd

class ChartGenerator:
    @staticmethod
    def generate_air_quality_chart(data):
        """Generate air quality trend chart using plotly."""
        df = pd.DataFrame(data)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['date'], y=df['pm25'],
                                mode='lines+markers',
                                name='PM2.5'))
        fig.add_trace(go.Scatter(x=df['date'], y=df['no2'],
                                mode='lines+markers',
                                name='NO₂'))
        
        fig.update_layout(
            title='Air Quality Trends',
            xaxis_title='Date',
            yaxis_title='Concentration (µg/m³)',
            template='plotly_white'
        )
        
        img_bytes = io.BytesIO()
        fig.write_image(img_bytes, format='png')
        img_bytes.seek(0)
        return img_bytes

    @staticmethod
    def generate_water_quality_chart(data):
        """Generate water quality trend chart."""
        df = pd.DataFrame(data)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['date'], y=df['ph'],
                                mode='lines+markers',
                                name='pH Level'))
        
        fig.update_layout(
            title='Water Quality Trends',
            xaxis_title='Date',
            yaxis_title='pH Level',
            template='plotly_white'
        )
        
        img_bytes = io.BytesIO()
        fig.write_image(img_bytes, format='png')
        img_bytes.seek(0)
        return img_bytes