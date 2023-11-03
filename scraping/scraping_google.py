
from scraper import Scraper

# abre o site de goolge com noticias do Brasil
url = "https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419"
new = Scraper(url)
new.scrape("gnews_br")

# abre o site de goolge com noticias internacionais
url = "https://news.google.com/news/rss/headlines"
new = Scraper(url)
new.scrape("gnews_world")
