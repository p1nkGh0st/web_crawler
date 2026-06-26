# main.py
"""
Main entry point for the Automated Daily Briefing Service.
"""
import schedule
import time
from datetime import datetime
import config  
import utils   

def run_daily_briefing():
    """The core coordination job that compiles data and triggers notifications."""
    print(f"\n=== ⏰ {datetime.now().strftime('%Y-%m-%d %H:%M')} Briefing Started ===")
    print("-" * 40)
    
    # 1. Compile data blocks from utils
    briefing_content = f"=== ⏰ Morning Briefing ===\n\n"
    briefing_content += utils.get_weather()
    briefing_content += utils.get_news_headlines_and_save()
    
    # 2. Print summary and send out the Discord notification
    print(briefing_content)
    utils.send_discord_notification(briefing_content)
    print("=== 😴 Job Finished. Returning to standby mode ===")


if __name__ == "__main__":
    print("⚡ Daily Briefing Service is now running...")
    print(f"🕒 Standby mode activated. Target time set to: {config.SCHEDULED_TIME}")
    
    # Test Rule: Run immediately once upon startup to verify system status
    run_daily_briefing()
    
    # Schedule Rule: Automated trigger from config setting
    schedule.every().day.at(config.SCHEDULED_TIME).do(run_daily_briefing)
    
    while True:
        schedule.run_pending()
        time.sleep(1)