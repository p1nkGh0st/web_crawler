# utils.py
"""
Utility functions for scraping data, saving Excel reports, and sending emails.
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import csv
import config  # 👈 Import our custom configurations

def get_weather():
    """Fetches real-time weather info for Los Angeles via wttr.in."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        response = requests.get(config.WEATHER_URL, headers=headers)
        lines = response.text.split("\n")

        weather_text = "N/A"
        for line in lines:
            if "Los Angeles:" in line:
                weather_text = BeautifulSoup(line, "html.parser").get_text().strip()
                break

        weather_report = "☀️ Today's Weather Summary (Los Angeles)\n"
        weather_report += f"- {weather_text}\n"
        weather_report += "-" * 40 + "\n"
        return weather_report
    except Exception as e:
        return f"❌ Error fetching weather data: {e}\n"


def get_news_headlines_and_save():
    """Fetches top 5 headlines and automatically saves them into a CSV file."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(config.NEWS_URL, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        raw_headlines = soup.find_all("a", attrs={"data-n-tid": True})
        if not raw_headlines:
            raw_headlines = [
                a for a in soup.select("article a") if len(a.get_text(strip=True)) > 15
            ]

        news_report = "📰 Today's Google Entertainment Headlines\n"
        unique_titles = []
        seen_keywords = set()

        for title in raw_headlines:
            clean_title = title.get_text(strip=True)

            if clean_title and clean_title not in unique_titles:
                words = clean_title.lower().split()
                keywords = {
                    w
                    for w in words
                    if len(w) > 3 and w not in ["from", "with", "that", "this", "after"]
                }

                if keywords & seen_keywords:
                    continue

                unique_titles.append(clean_title)
                seen_keywords.update(keywords)

            if len(unique_titles) == 5:
                break

        # [1-Click Upgrade] Auto-save Google News to CSV
        today_date = datetime.now().strftime('%Y%m%d_%H%M')
        filename = f"google_news_{today_date}.csv"
        
        with open(filename, mode="w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["No.", "Headline"])
            
            for idx, title in enumerate(unique_titles, 1):
                writer.writerow([idx, title])
                news_report += f"{idx}. {title}\n"
        
        print(f"💾 [SUCCESS] Excel report saved as: {filename}")
        news_report += "-" * 40 + "\n"
        return news_report
    except Exception as e:
        return f"❌ Error fetching news headlines: {e}\n"


def send_email_notification(content):
    """Sends the compiled briefing content directly to your Gmail inbox."""
    today_str = datetime.now().strftime('%Y-%m-%d %H:%M')
    msg = MIMEText(content, "plain", "utf-8")
    msg["Subject"] = f"☕ Daily Briefing Report ({today_str})"
    msg["From"] = config.SENDER_EMAIL
    msg["To"] = config.RECEIVER_EMAIL
    
    try:
        with smtplib.SMTP_SSL(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.login(config.SENDER_EMAIL, config.APP_PASSWORD)
            server.sendmail(config.SENDER_EMAIL, config.RECEIVER_EMAIL, msg.as_string())
        print("🚀 Briefing email has been successfully delivered to your inbox!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")