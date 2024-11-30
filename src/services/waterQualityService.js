import moment from 'moment';

export function getWaterQuality() {
  return {
    pH: +(Math.random() * (9.0 - 6.0) + 6.0).toFixed(2),
    turbidity: +(Math.random() * 10).toFixed(2),
    temperature: +(Math.random() * (30 - 15) + 15).toFixed(2),
    timestamp: moment().format()
  };
}