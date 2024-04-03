import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.imdb.com/chart/starmeter/?ref_=nv_cel_m' 
browser = webdriver.Chrome()
browser.get(url)

xpath = '//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li' 

WebDriverWait(browser, 50).until(
    EC.presence_of_all_elements_located((By.XPATH, xpath))
)

celebs = browser.find_elements(By.XPATH, xpath)

celebs_data = [["Rank", "Name", "Role(s)", "Example Movie"]]

for celeb in celebs:
    text_lines = celeb.text.split('\n')
    if len(text_lines) >= 4: 
        rank = text_lines[0].split(' ')[0] 
        name = text_lines[3] 
        roles = ', '.join(text_lines[4:-1]) 
        example_movie = text_lines[-1] 
        
        celebs_data.append([rank, name, roles, example_movie])


with open('imdb_top_100_celebs.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(celebs_data)

browser.quit()