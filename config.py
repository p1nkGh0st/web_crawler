import os

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")
CRYPTO_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple&vs_currencies=usd&include_24hr_change=true"
CRYPTO_API_KEY = os.environ.get("CRYPTO_API_KEY")
SCHEDULED_TIME = os.environ.get("SCHEDULED_TIME", "14:00")
