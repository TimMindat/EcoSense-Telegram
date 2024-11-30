import { getWaterQuality } from '../services/waterQualityService.js';
import { formatWaterQualityMessage } from '../utils/messageFormatter.js';

export async function handleWaterQuality(bot, msg) {
  const chatId = msg.chat.id;
  try {
    const data = await getWaterQuality();
    const message = formatWaterQualityMessage(data);
    
    const opts = {
      reply_markup: {
        inline_keyboard: [
          [{ text: 'Refresh Data', callback_data: 'refresh_water' }],
          [{ text: 'View Trends', callback_data: 'water_charts' }]
        ]
      }
    };

    bot.sendMessage(chatId, message, opts);
  } catch (error) {
    bot.sendMessage(chatId, '⚠️ Unable to fetch water quality data. Please try again later.');
  }
}