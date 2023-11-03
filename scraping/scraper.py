
import urllib.request
from bs4 import BeautifulSoup

conteudo = ""

class Scraper:
    """
    Modelando um webscraping de um site
    """
    def __init__(self, site: str):
        """
        Inicializa os atributos.
        recebe como parâmetro o site a partir do qual será feito o scraping.
        :param site: str url do site do qual se deseja fazer o scraping
        """
        self.site = site
     

    def scrape(self, nome_arquivo: str):
        """
        Salva um arquivo txt com o texto extraído do site passado como parametro.
        :param nome_arquivo: str - nome para salvar o arquivo (sem a extensão)
        """
        r = urllib.request.urlopen(self.site)

        xml = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(xml,parser)
        nome_arquivo = nome_arquivo  + ".txt"

        with open(nome_arquivo, "w",-1,"utf-8") as f:
            for item in sp.find_all("item"):
                title = item.find("title")
                if title is None:
                    continue
                else:
                    print("\n" + title.text)
                    f.write(title.text + "\n\n")

