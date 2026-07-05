# config.py
"""
Configuration settings for the Daily Briefing Web Crawler.
Keep your sensitive credentials and fixed settings here.
"""

# Discord Webhook URLs
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1520178279129022546/XyyIHJeFxfyCW_jaMznXHBAkTDI4zc7FdBoQ0BHkL2FDTUIzI8SsafJeMnO2eIBVgp-Y"

# Crypto API endpoint for BTC, ETH, and XRP price and 24h change data
CRYPTO_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple&vs_currencies=usd&include_24hr_change=true"

# Scheduler Settings
SCHEDULED_TIME = "14:00"
