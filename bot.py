"""Main bot application."""
import logging
import asyncio
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from config import BOT_TOKEN
from handlers import (
    start_command,
    help_command,
    air_quality_command,
    water_quality_command,
    charts_command,
    callback_query_handler
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

async def main():
    """Start the bot."""
    # Create the Application
    app = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("air_quality", air_quality_command))
    app.add_handler(CommandHandler("water_quality", water_quality_command))
    app.add_handler(CommandHandler("charts", charts_command))
    
    # Add callback query handler for inline buttons
    app.add_handler(CallbackQueryHandler(callback_query_handler))

    # Start the bot
    print("Starting EcoSense Bot...")
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())