# 🤖 Multifunctional Telegram Bot

A Telegram bot with weather forecasts, currency rates, news and automatic weather alerts.

## 🚀 Features
- 🌤 Weather forecast for 3 days with feels-like temperature scale
- ⚠️ Automatic weather alerts (storm, rain, frost, heat, UV index)
- 💶 Currency exchange rates (EUR base)
- 📰 Latest news from Deutsche Welle
- 🔔 Background notifications — bot warns you even when you are offline
- 📍 Saves your city for automatic hourly weather checks

## 📦 Installation
\\\
pip install -r requirements.txt
\\\

## ⚙️ Configuration
Create a .env file:
\\\
TELEGRAM_TOKEN=your_telegram_token
WEATHER_API_KEY=your_openweathermap_key
\\\

## ▶️ Usage
\\\
python telegram_bot.py
\\\

## 🛠 Tech Stack
- Python 3.11
- pyTelegramBotAPI
- requests
- BeautifulSoup4
- python-dotenv
- schedule
