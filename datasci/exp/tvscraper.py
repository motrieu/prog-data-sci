import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.imdb.com/title/tt0099785/reviews?ref_=tt_urv'
browser = webdriver.Chrome()
browser.get(url)

load_more_button_xpath = '//*[@id="load-more-trigger"]'

def click_load_more_button(browser):
    try:
        load_more_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, load_more_button_xpath))
        )
        if load_more_button:
            browser.execute_script("arguments[0].click();", load_more_button)
            return True
    except Exception as e:
        print("Error clicking 'Load More':", e)
    return False

def load_more_reviews(browser, attempts=5):
    for _ in range(attempts):
        if not click_load_more_button(browser):
            break  
        time.sleep(2) 

load_more_reviews(browser)

xpath_reviews = '//*[@id="main"]/section/div[2]/div[2]/div'
WebDriverWait(browser, 50).until(
    EC.presence_of_all_elements_located((By.XPATH, xpath_reviews))
)

reviews = browser.find_elements(By.XPATH, xpath_reviews)
reviews_data = [["Rating", "Title", "Username", "Date", "Review"]]

date_pattern = re.compile(r'\d{1,2}\s\w+\s\d{4}')

for review in reviews:
    text = review.text
    if "Warning: Spoilers" in text or "No more 'Load More' button found" in text:
        continue

    text = re.sub(r'\d+ out of \d+ found this helpful. Was this review helpful\? Sign in to vote. Permalink', '', text, flags=re.IGNORECASE)

    parts = text.split('\n')
    rating = parts[0].split('/')[0] if '/' in parts[0] else "no rating"
    date_match = date_pattern.search(text)
    date = date_match.group() if date_match else "Date unknown"
    title_index = 1 if rating != "no rating" else 0
    title = parts[title_index]
    username = parts[title_index + 1].split(' ')[0]
    review_text = ' '.join(parts[title_index + 2:])

    reviews_data.append([rating, title, username, date, review_text])

with open('home_alone_reviews_enhanced.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(reviews_data)

browser.quit()