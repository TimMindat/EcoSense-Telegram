"""Message handlers for the EcoSense Telegram bot."""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.api_client import APIClient
from utils.chart_generator import ChartGenerator
import json

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command."""
    welcome_message = (
        "🌍 Welcome to EcoSense Bot!\n\n"
        "I provide real-time environmental data and health recommendations. "
        "Here's what I can do:\n\n"
        "📊 /air_quality - Get real-time air quality data\n"
        "💧 /water_quality - Check water quality metrics\n"
        "📈 /charts - View environmental trends\n"
        "⚙️ /settings - Configure notifications\n"
        "❓ /help - Show all commands\n\n"
        "Let's start monitoring our environment together! 🌱"
    )
    keyboard = [
        [
            InlineKeyboardButton("Air Quality", callback_data='air_quality'),
            InlineKeyboardButton("Water Quality", callback_data='water_quality')
        ],
        [InlineKeyboardButton("View Charts", callback_data='charts')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

async def air_quality_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /air_quality command."""
    api_client = APIClient()
    data = api_client.fetch_air_quality()
    
    if not data:
        await update.message.reply_text("⚠️ Unable to fetch air quality data. Please try again later.")
        return

    message = (
        "🌬️ Current Air Quality in Cairo:\n\n"
        f"PM2.5: {data[0]['value']} µg/m³\n"
        f"NO₂: {data[1]['value']} ppb\n"
        f"SO₂: {data[2]['value']} ppb\n"
        f"CO: {data[3]['value']} ppm\n\n"
    )

    # Add health recommendation based on PM2.5 levels
    if data[0]['value'] > 55.4:
        message += "🚨 Warning: Air quality is unhealthy. Consider staying indoors."
    elif data[0]['value'] > 35.4:
        message += "⚠️ Moderate air quality. Sensitive groups should reduce outdoor activity."
    else:
        message += "✅ Air quality is good. Enjoy outdoor activities!"

    keyboard = [
        [InlineKeyboardButton("Refresh Data", callback_data='refresh_air')],
        [InlineKeyboardButton("View Trends", callback_data='air_charts')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message, reply_markup=reply_markup)

async def water_quality_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /water_quality command."""
    api_client = APIClient()
    data = api_client.simulate_water_quality()
    
    message = (
        "💧 Current Water Quality Metrics:\n\n"
        f"pH Level: {data['pH']}\n"
        f"Turbidity: {data['turbidity']} NTU\n"
        f"Temperature: {data['temperature']}°C\n\n"
    )

    # Add recommendations based on water quality
    if not (6.5 <= data['pH'] <= 8.5):
        message += "⚠️ pH levels are outside the optimal range. Water treatment recommended."
    else:
        message += "✅ Water quality parameters are within safe limits."

    keyboard = [
        [InlineKeyboardButton("Refresh Data", callback_data='refresh_water')],
        [InlineKeyboardButton("View Trends", callback_data='water_charts')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(message, reply_markup=reply_markup)

async def charts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /charts command."""
    api_client = APIClient()
    chart_generator = ChartGenerator()
    
    # Generate and send air quality chart
    historical_data = api_client.get_historical_data()
    air_chart = chart_generator.generate_air_quality_chart(historical_data)
    await update.message.reply_photo(
        photo=air_chart,
        caption="📊 Air Quality Trends (Last 7 Days)"
    )
    
    # Generate and send water quality chart
    water_chart = chart_generator.generate_water_quality_chart(historical_data)
    await update.message.reply_photo(
        photo=water_chart,
        caption="📈 Water Quality Trends (Last 7 Days)"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /help command."""
    help_text = (
        "🌟 Available Commands:\n\n"
        "/start - Get started with EcoSense Bot\n"
        "/air_quality - Get real-time air quality data\n"
        "/water_quality - Check water quality metrics\n"
        "/charts - View environmental trends\n"
        "/settings - Configure notification preferences\n"
        "/help - Show this help message\n\n"
        "💡 Tip: Use the inline buttons below messages for quick actions!"
    )
    await update.message.reply_text(help_text)

async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle callback queries from inline buttons."""
    query = update.callback_query
    await query.answer()
    
    if query.data == 'air_quality':
        await air_quality_command(update, context)
    elif query.data == 'water_quality':
        await water_quality_command(update, context)
    elif query.data == 'charts':
        await charts_command(update, context)
    elif query.data.startswith('refresh_'):
        if query.data == 'refresh_air':
            await air_quality_command(update, context)
        else:
            await water_quality_command(update, context)