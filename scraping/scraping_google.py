
from scraper import Scraper

url = "https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419"
# url = "https://news.google.com/news/rss/headlines"

new = Scraper(url)
new.scrape()