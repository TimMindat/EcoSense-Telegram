# EcoSense Telegram Bot

A comprehensive environmental monitoring bot that provides real-time air and water quality data, interactive charts, and health recommendations.

## Features

- Real-time air quality monitoring
- Water quality metrics
- Interactive data visualization
- Health recommendations
- Push notifications for environmental alerts
- Inline buttons for easy navigation

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Get a Telegram Bot Token:
   - Open Telegram and search for @BotFather
   - Start a chat and use /newbot command
   - Follow the instructions to create a new bot
   - Copy the token provided by BotFather

3. Configure the bot:
   - Create a `.env` file in the project root
   - Add your bot token: `BOT_TOKEN=your_token_here`

4. Run the bot:
   ```bash
   python bot.py
   ```

## Available Commands

- `/start` - Get started with EcoSense Bot
- `/air_quality` - Get real-time air quality data
- `/water_quality` - Check water quality metrics
- `/charts` - View environmental trends
- `/settings` - Configure notification preferences
- `/help` - Show all available commands

## Data Sources

- Air Quality Data: OpenAQ API
- Water Quality Data: Simulated data (can be replaced with real data source)

## Project Structure

- `bot.py` - Main application file
- `config.py` - Configuration settings
- `handlers.py` - Command handlers
- `utils/`
  - `api_client.py` - API integration
  - `chart_generator.py` - Chart generation utilities