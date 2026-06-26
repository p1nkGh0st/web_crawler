# 🌤️ Daily Briefing & Discord Alert Web Crawler

A lightweight, automated Python-based web crawler that fetches real-time weather summaries, scrapes top headlines, archives them into an Excel-ready CSV format, and instantly delivers the compiled report directly to your Discord channel.

## 🚀 Features
- **Real-time Weather Summary:** Fetches the current weather description for Los Angeles in a clean, plain-text format using `wttr.in`.
- **Google News Headlines Scraper:** Dynamically extracts the top 5 entertainment headlines using `BeautifulSoup` and semantic HTML selector tracking.
- **Smart Keyword Filtering:** Implements an advanced keyword-based de-duplication mechanism to filter out overlapping topics and guarantee 5 unique articles.
- **Automated CSV Archiving:** Automatically converts and exports daily scraped news into a beautifully formatted, timestamped CSV file (`.csv`) for data logging.
- **Instant Discord Integration:** Delivers the fully compiled morning report straight to your smartphone or desktop via a seamless Discord Inbound Webhook bypass.
- **24/7 Automation Scheduler:** Runs continuously in standby mode, automatically triggering the daily briefing at your precise custom target time using the `schedule` engine.

## 🛠️ Tech Stack & Requirements
- **Language:** Python 3.x
- **Libraries Used:** - `requests` (for secure HTTP data transmission & webhook triggers)
  - `beautifulsoup4` (for advanced HTML DOM parsing)
  - `schedule` (for precise interval time management)

## 💻 How to Run
1. Clone this repository to your local machine.
2. Install the required external dependencies:
   ```bash
   pip install requests beautifulsoup4 schedule