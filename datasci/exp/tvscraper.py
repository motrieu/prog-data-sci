import csv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.imdb.com/title/tt0099785/reviews?ref_=tt_urv'
browser = webdriver.Chrome()
browser.get(url)

xpath_reviews = '//*[@id="main"]/section/div[2]/div[2]/div'
WebDriverWait(browser, 50).until(
    EC.presence_of_all_elements_located((By.XPATH, xpath_reviews))
)

reviews = browser.find_elements(By.XPATH, xpath_reviews)
reviews_data = [["Rating", "Title", "Username", "Date", "Review"]]

date_pattern = re.compile(r'\d{1,2}\s\w+\s\d{4}')  

for review in reviews:
    text = review.text
    if "Warning: Spoilers" in text:
        continue

    text = re.sub(r'\d+ out of \d+ found this helpful. Was this review helpful\? Sign in to vote. Permalink', '', text, flags=re.IGNORECASE)

    parts = text.split('\n')
    rating = parts[0].split('/')[0] if '/' in parts[0] else "no rating"
    
    date_match = date_pattern.search(text)
    if date_match:
        date = date_match.group()
    else:
        date = "Date unknown"  

    title_index = 1 if rating != "no rating" else 0
    title = parts[title_index]
    
    username = parts[title_index + 1].split(' ')[0]

    review_text = ' '.join(parts[title_index + 2:])
    
    reviews_data.append([rating, title, username, date, review_text])

with open('home_alone_reviews_fixed.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(reviews_data)

browser.quit()