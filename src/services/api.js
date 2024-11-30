const axios = require('axios');
const moment = require('moment');

const OPENAQ_API_URL = 'https://api.openaq.org/v2/measurements';
const DEFAULT_LOCATION = {
  city: 'Cairo',
  coordinates: { latitude: 30.0444, longitude: 31.2357 }
};

async function getAirQuality() {
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

function getWaterQuality() {
  // Simulate water quality data
  return {
    pH: +(Math.random() * (9.0 - 6.0) + 6.0).toFixed(2),
    turbidity: +(Math.random() * 10).toFixed(2),
    temperature: +(Math.random() * (30 - 15) + 15).toFixed(2),
    timestamp: moment().format()
  };
}

function getHistoricalData(days = 7) {
  const data = [];
  for (let i = 0; i < days; i++) {
    data.push({
      date: moment().subtract(i, 'days').format('YYYY-MM-DD'),
      pm25: Math.random() * (150 - 10) + 10,
      no2: Math.random() * (200 - 20) + 20,
      ph: Math.random() * (8.5 - 6.5) + 6.5
    });
  }
  return data;
}

module.exports = {
  getAirQuality,
  getWaterQuality,
  getHistoricalData
};