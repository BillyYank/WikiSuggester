from bs4 import BeautifulSoup as bs
import requests
import sys
import urllib2
import networkx as nx
from lxml import html
import re


class Parser:
    def get_url_from_name(self, name):
        return "https://en.wikipedia.org/wiki/" + name
    
    def get(self, name):
        url = self.get_url_from_name(name)
        page = urllib2.urlopen(url).read()
        soup = bs(page, 'html.parser')
        refs = soup.findAll('a', href=re.compile('/wiki/*'))
        for ref in refs:
            yield str(ref).split('/')[2].split("\"")[0]


#parser = Parser()
#parser.get("John_Lennon")
