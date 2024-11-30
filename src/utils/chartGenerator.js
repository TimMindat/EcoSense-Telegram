const { ChartJSNodeCanvas } = require('chartjs-node-canvas');
const { getHistoricalData } = require('../services/api');

const width = 800;
const height = 400;

const chartJSNodeCanvas = new ChartJSNodeCanvas({ width, height });

async function generateCharts() {
  const data = getHistoricalData();
  
  const airQualityChart = await generateAirQualityChart(data);
  const waterQualityChart = await generateWaterQualityChart(data);
  
  return {
    airQuality: airQualityChart,
    waterQuality: waterQualityChart
  };
}

async function generateAirQualityChart(data) {
  const configuration = {
    type: 'line',
    data: {
      labels: data.map(d => d.date),
      datasets: [
        {
          label: 'PM2.5',
          data: data.map(d => d.pm25),
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        },
        {
          label: 'NO₂',
          data: data.map(d => d.no2),
          borderColor: 'rgb(255, 99, 132)',
          tension: 0.1
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Air Quality Trends'
        }
      }
    }
  };

  return await chartJSNodeCanvas.renderToBuffer(configuration);
}

async function generateWaterQualityChart(data) {
  const configuration = {
    type: 'line',
    data: {
      labels: data.map(d => d.date),
      datasets: [{
        label: 'pH Level',
        data: data.map(d => d.ph),
        borderColor: 'rgb(54, 162, 235)',
        tension: 0.1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Water Quality Trends'
        }
      }
    }
  };

  return await chartJSNodeCanvas.renderToBuffer(configuration);
}

module.exports = {
  generateCharts
};