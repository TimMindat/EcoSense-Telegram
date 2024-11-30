import { generateCharts } from '../utils/chartGenerator.js';

export async function handleCharts(bot, msg) {
  const chatId = msg.chat.id;
  try {
    const charts = await generateCharts();
    await bot.sendPhoto(chatId, charts.airQuality, { caption: '📊 Air Quality Trends (Last 7 Days)' });
    await bot.sendPhoto(chatId, charts.waterQuality, { caption: '📈 Water Quality Trends (Last 7 Days)' });
  } catch (error) {
    bot.sendMessage(chatId, '⚠️ Unable to generate charts. Please try again later.');
  }
}