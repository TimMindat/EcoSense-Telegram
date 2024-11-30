import { getAirQuality } from '../services/airQualityService.js';
import { formatAirQualityMessage } from '../utils/messageFormatter.js';

export async function handleAirQuality(bot, msg) {
  const chatId = msg.chat.id;
  try {
    const data = await getAirQuality();
    const message = formatAirQualityMessage(data);
    
    const opts = {
      reply_markup: {
        inline_keyboard: [
          [{ text: 'Refresh Data', callback_data: 'refresh_air' }],
          [{ text: 'View Trends', callback_data: 'air_charts' }]
        ]
      }
    };

    bot.sendMessage(chatId, message, opts);
  } catch (error) {
    bot.sendMessage(chatId, '⚠️ Unable to fetch air quality data. Please try again later.');
  }
}