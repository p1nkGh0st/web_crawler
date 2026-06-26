# config.example.py
"""
[Template] Configuration settings for the Daily Briefing Web Crawler.
Instructions: Copy this file, rename it to 'config.py', and fill in your details.
"""

# Discord Webhook URLs
DISCORD_WEBHOOK_URL = "XXXXXXXXXXXXXXXXXXX" # Replace with your discord webhook

# Crawler Source URLs (Pre-configured)
WEATHER_URL = "https://wttr.in/Los+Angeles?format=3"
NEWS_URL = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

# Scheduler Settings (Default)
SCHEDULED_TIME = "10:00"