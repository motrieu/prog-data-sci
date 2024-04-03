import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.imdb.com/chart/top/'
browser = webdriver.Chrome()
browser.get(url)

xpath = '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li'

WebDriverWait(browser, 50).until(
    EC.presence_of_all_elements_located((By.XPATH, xpath))
)

movies = browser.find_elements(By.XPATH, xpath)


movies_data = [["Rank", "Title", "Release Year", "Duration", "Age Rating", "Rating", "Amount of Reviews"]]

for movie in movies:
    details = movie.text.split('\n')
    rank_title = details[0].split('. ', 1)
    rank = rank_title[0]
    title = rank_title[1]
    release_year = details[1]
    duration = details[2]
    age_rating = details[3]
    rating = details[4]
    amount_of_reviews = details[5].strip(' ()').replace('K', '000')  
    
    movies_data.append([rank, title, release_year, duration, age_rating, rating, amount_of_reviews])


with open('imdb_top_250.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(movies_data)

browser.quit()