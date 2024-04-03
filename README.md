# Final Project for Course "Programming in Data Science" UPM 2nd Semester 2024
Members:
 - Sigrid Festoy
 - Sebastian Montenius
 - Yu Xindi
 - Huang Tongyi
 - Moritz Trieu

 Python Version: 3.11.4

Further documentation and results, not contained in this repo can be found under:
https://docs.google.com/document/d/16j4VfSlvhqssUdWIX4S-B2k7sDmYypXg7qdXDZHerwY/edit?usp=sharing

# Contents

This module contains the functionality and output of webscraping in the project. It contains: 

 - datasci/exp folder: Contains the scripts scraping the top 250 movies on IMDb, the top 100 celebs and the reviews fo the movie "Home Alone".
 - 


# How to run
Before you run the code, it can be beneficial to have set up a virtual environment. Make sure your VS code interpreter is set to this python bin. If you use the command line make sure to activate the environment before running any python operations by

- Linux/ Mac: ./venv/scripts/activate
- Win: ./venv/scripts/Activate.ps1

After you have activated your virtual environment, you can start running the code. Navigate into the directory and execute each script seperately. 

 - To scrape top 250 movies: run movie_scraper.py through your IDE or using: python movie_scraper.py in the terminal

 - To scrape top 100 celebs: run celeb_scraper.py through your IDE or using: python celeb_scraper.py in the terminal

 - To scrape reviews of "Home Alone": run ha_scraper.py through your IDE or using: python ha_scraper.py in the terminal

The csv files will show up in the root folder. 

