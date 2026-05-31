"""
Day 77 Milestone Project: E-Commerce Price Tracker & Spreadsheet Exporter 🛒
----------------------------------------------------------------------------
Combine HTML parsing (BeautifulSoup), HTTP request triggers, and CSV file writes 
by engineering an automated E-Commerce Price Tracker.

Task Requirements:
1. Use 'requests' to fetch raw HTML pages from a mock shopping catalog.
   - For student practice, we'll scrape a free, public sandbox catalog:
     https://books.toscrape.com/
2. Parse HTML page elements using 'BeautifulSoup'.
3. Extract book titles, stock availability, and price details.
4. Filter books with prices below £20.00.
5. Export the filtered collection to a CSV spreadsheet.
"""

from bs4 import BeautifulSoup
import requests
import csv

CATALOG_URL = "https://books.toscrape.com/"

def run_price_tracker():
    print(f"=== Scraping Catalog: {CATALOG_URL} ===")
    
    try:
        response = requests.get(CATALOG_URL, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # TODO: Parse catalog products
        # 1. Identify product containers (hint: look for <article class="product_pod">)
        # 2. Extract Title, Price, and Availability
        # 3. Print extracted results
        # 4. Save results to a local CSV file: 'catalog_books.csv'
        pass
    except requests.exceptions.RequestException as e:
        print(f"❌ Scraping Failed: {e}")

if __name__ == "__main__":
    run_price_tracker()
