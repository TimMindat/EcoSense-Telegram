export function handleHelp(bot, msg) {
  const chatId = msg.chat.id;
  const helpMessage = 
    '🌟 Available Commands:\n\n' +
    '/start - Get started with EcoSense Bot\n' +
    '/air_quality - Get real-time air quality data\n' +
    '/water_quality - Check water quality metrics\n' +
    '/charts - View environmental trends\n' +
    '/help - Show this help message\n\n' +
    '💡 Tip: Use the inline buttons below messages for quick actions!';

  bot.sendMessage(chatId, helpMessage);
}