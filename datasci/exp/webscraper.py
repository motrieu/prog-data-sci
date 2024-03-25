
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = 'https://www.imdb.com/chart/top/'
browser = webdriver.Chrome()
browser.get(url)

xpath = '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul'

WebDriverWait(browser, 50).until(
    EC.presence_of_element_located((By.XPATH, xpath))
)

movies = browser.find_elements(By.XPATH, xpath)

for movie in movies:
    print(movie.text)

browser.quit()
