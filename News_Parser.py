import requests
#For Web-Scraping
from bs4 import BeautifulSoup


URL = 'https://www.crunchyroll.com/news'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('h2')
news_title1 = results[0]
news_title2 = results[1]
news_title3 = results[2]
news_title4 = results[3]
news_title5 = results[4]

#WEB SCRAPING FOR LINKS FROM THE TITLES
news_links1 = results[0].find('a')
news_link1 = news_links1.get('href')
news_links2 = results[1].find('a')
news_link2 = news_links2.get('href')
news_links3 = results[2].find('a')
news_link3 = news_links3.get('href')
news_links4 = results[3].find('a')
news_link4 = news_links4.get('href')
news_links5 = results[4].find('a')
news_link5 = news_links5.get('href')

