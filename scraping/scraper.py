
import urllib.request
from bs4 import BeautifulSoup

conteudo = ""

class Scraper:
    """
    Modelando um webscraping de um site
    """
    def __init__(self,site):
        """
        Inicializa os atributos.
        recebe como parâmetro o site a partir do qual será feito o scraping
        """
        self.site = site

    def scrape(self):
        """
        Este método será chamado sempre que quisermos fazer um scraping no site passado como parametro.
        A função urlopen() faz uma solicitação a um site e retorna um objeto Response que contém o xml armazenado com todos os dados adicionais.
        A função read() retorna o XML do objeto Response. Todo o XML do site está na variável xml
        """
        r = urllib.request.urlopen(self.site)

        xml = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(xml,parser)

        with open("noticias_google.txt", "w",-1,"utf-8") as f:
            for item in sp.find_all("item"):
                title = item.find("title")
                if title is None:
                    continue
                else:
                    print("\n" + title.text)
                    f.write(title.text + "\n\n")

