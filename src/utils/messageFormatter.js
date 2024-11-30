function formatAirQualityMessage(data) {
  if (!data) {
    return '⚠️ Unable to fetch air quality data. Please try again later.';
  }

  const message = 
    '🌬️ Current Air Quality in Cairo:\n\n' +
    `PM2.5: ${data[0].value} µg/m³\n` +
    `NO₂: ${data[1].value} ppb\n` +
    `SO₂: ${data[2].value} ppb\n` +
    `CO: ${data[3].value} ppm\n\n`;

  // Add health recommendation based on PM2.5 levels
  if (data[0].value > 55.4) {
    return message + '🚨 Warning: Air quality is unhealthy. Consider staying indoors.';
  } else if (data[0].value > 35.4) {
    return message + '⚠️ Moderate air quality. Sensitive groups should reduce outdoor activity.';
  }
  return message + '✅ Air quality is good. Enjoy outdoor activities!';
}

function formatWaterQualityMessage(data) {
  const message = 
    '💧 Current Water Quality Metrics:\n\n' +
    `pH Level: ${data.pH}\n` +
    `Turbidity: ${data.turbidity} NTU\n` +
    `Temperature: ${data.temperature}°C\n\n`;

  // Add recommendations based on water quality
  if (data.pH < 6.5 || data.pH > 8.5) {
    return message + '⚠️ pH levels are outside the optimal range. Water treatment recommended.';
  }
  return message + '✅ Water quality parameters are within safe limits.';
}

module.exports = {
  formatAirQualityMessage,
  formatWaterQualityMessage
};