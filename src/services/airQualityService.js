import axios from 'axios';
import { OPENAQ_API_URL, DEFAULT_LOCATION } from '../config/constants.js';

export async function getAirQuality() {
  try {
    const response = await axios.get(OPENAQ_API_URL, {
      params: {
        city: DEFAULT_LOCATION.city,
        limit: 100,
        parameter: ['pm25', 'no2', 'so2', 'co']
      }
    });
    return response.data.results;
  } catch (error) {
    console.error('Error fetching air quality data:', error);
    return null;
  }
}