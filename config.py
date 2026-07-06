# config.py
"""
Configuration settings for the Daily Briefing Web Crawler.
Keep your sensitive credentials and fixed settings here.
"""

# Discord Webhook URLs
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1523807626616639590/CfoSKL_oYWR2jqWMz-AiFoEMXqrV8f1k8ffJzZuNcLyk6BalTz6P8qEkdBKHK1XrN8pP"

# Crypto API endpoint for BTC, ETH, and XRP price and 24h change data
CRYPTO_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple&vs_currencies=usd&include_24hr_change=true"

# Scheduler Settings
SCHEDULED_TIME = "15:05"
