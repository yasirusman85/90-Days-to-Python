# 🟠 Week 11: Web Scraping & Automation

Welcome to Week 11! 🚀 This week is all about saving time by automating manual computer operations. You will learn to extract raw information from public websites using **BeautifulSoup**, navigate complex interactive pages with browser controllers (**Selenium** or **Playwright**), orchestrate operating system file operations, and set up automatic task schedulers.

---

## 📅 Weekly Schedule

| Day | Topic | Key Focus | Project / Challenge |
| :--- | :--- | :--- | :--- |
| **Day 71** | [HTML & Ethics](#day-71-html-and-scraping-ethics) | Tags, IDs, selectors, `robots.txt` guidelines | Rules validator script |
| **Day 72** | [BeautifulSoup](#day-72-beautifulsoup) | Extracting titles, prices, and links | Quote-of-the-day harvester |
| **Day 73** | [Pagination](#day-73-scraping-pagination) | Loops across multi-page layouts | Book inventory collector |
| **Day 74** | [Browser Control](#day-74-browser-automation) | Selenium/Playwright clicks and input submits | Automated portal login |
| **Day 75** | [OS Automation](#day-75-os-level-scripts) | File renaming, sorting, email alerts | Clean download folder script |
| **Day 76** | [Job Scheduling](#day-76-task-scheduling) | `schedule` library, cron, task schedulers | Periodic system checker |
| **Day 77** | [Milestone Project](#day-77-milestone-project-e-commerce-price-tracker) | Scrape and save structured data | **E-Commerce Price Tracker** |

---

## 📖 Daily Lessons

### Day 72: Scraping with BeautifulSoup
BeautifulSoup parses HTML elements, allowing you to search for specific elements by their tags, IDs, or CSS classes:
```python
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("span", class_="titleline")
for item in articles[:5]:
    print(item.text)
```

### Day 74: Browser Automation
Dynamic JavaScript websites require real-time browser execution. Use Selenium or Playwright to control a virtual browser window, click elements, fill in forms, and read live web content.

### Day 76: Job Scheduling
Run scripts automatically at specific intervals without manual intervention:
```python
import schedule
import time

def job():
    print("Running recurring maintenance task...")

schedule.every().day.at("09:00").do(job)
```

---

### Day 77: Milestone Project: E-Commerce Price Tracker
Build a scraper that monitors the price of a specific online product. If the price drops below your target budget, the script should automatically generate an email alert. The final dataset should be formatted and exported to an Excel/CSV spreadsheet.
