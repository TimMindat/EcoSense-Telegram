export function handleStart(bot, msg) {
  const chatId = msg.chat.id;
  const welcomeMessage = 
    '🌍 Welcome to EcoSense Bot!\n\n' +
    'I provide real-time environmental data and health recommendations.\n\n' +
    'Available commands:\n' +
    '📊 /air_quality - Get real-time air quality data\n' +
    '💧 /water_quality - Check water quality metrics\n' +
    '📈 /charts - View environmental trends\n' +
    '❓ /help - Show all commands\n\n' +
    'Let\'s start monitoring our environment together! 🌱';

  const opts = {
    reply_markup: {
      inline_keyboard: [
        [
          { text: 'Air Quality', callback_data: 'air_quality' },
          { text: 'Water Quality', callback_data: 'water_quality' }
        ],
        [{ text: 'View Charts', callback_data: 'charts' }]
      ]
    }
  };

  bot.sendMessage(chatId, welcomeMessage, opts);
}