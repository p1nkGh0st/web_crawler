# config.example.py
"""
[Template] Configuration settings for the Daily Briefing Web Crawler.
Instructions: Copy this file, rename it to 'config.py', and fill in your details.
"""

# Email Settings (Optional)
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_16_digit_app_password"
RECEIVER_EMAIL = "your_email@gmail.com"

# SMTP Server Configurations
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Crawler Source URLs (Pre-configured)
WEATHER_URL = "https://wttr.in/Los+Angeles?format=3"
NEWS_URL = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

# Scheduler Settings (Default)
SCHEDULED_TIME = "08:30"