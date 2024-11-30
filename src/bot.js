import TelegramBot from 'node-telegram-bot-api';
import { handleStart } from './handlers/startHandler.js';
import { handleAirQuality } from './handlers/airQualityHandler.js';
import { handleWaterQuality } from './handlers/waterQualityHandler.js';
import { handleCharts } from './handlers/chartsHandler.js';
import { handleHelp } from './handlers/helpHandler.js';
import { handleCallbackQuery } from './handlers/callbackQueryHandler.js';

export function startBot() {
  const bot = new TelegramBot(process.env.BOT_TOKEN, { polling: true });

  // Register command handlers
  bot.onText(/\/start/, (msg) => handleStart(bot, msg));
  bot.onText(/\/air_quality/, (msg) => handleAirQuality(bot, msg));
  bot.onText(/\/water_quality/, (msg) => handleWaterQuality(bot, msg));
  bot.onText(/\/charts/, (msg) => handleCharts(bot, msg));
  bot.onText(/\/help/, (msg) => handleHelp(bot, msg));

  // Register callback query handler
  bot.on('callback_query', (query) => handleCallbackQuery(bot, query));

  console.log('EcoSense Bot is running...');
  return bot;
}