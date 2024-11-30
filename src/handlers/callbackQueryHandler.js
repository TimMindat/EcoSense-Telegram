import { handleAirQuality } from './airQualityHandler.js';
import { handleWaterQuality } from './waterQualityHandler.js';
import { handleCharts } from './chartsHandler.js';

export async function handleCallbackQuery(bot, query) {
  const chatId = query.message.chat.id;
  
  switch (query.data) {
    case 'air_quality':
      await handleAirQuality(bot, { chat: { id: chatId } });
      break;
    case 'water_quality':
      await handleWaterQuality(bot, { chat: { id: chatId } });
      break;
    case 'charts':
      await handleCharts(bot, { chat: { id: chatId } });
      break;
  }
  
  bot.answerCallbackQuery(query.id);
}