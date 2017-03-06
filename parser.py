from bs4 import BeautifulSoup as bs
import requests
import sys
import urllib2
import networkx as nx
from lxml import html
import re
import urllib


class Parser:
    def filter(self, url):
        bad_words = [
                     'Main_Page',
                     ':',
                     ".org",
                     "International_Standard_Book_Number"
                     ]
        for word in bad_words:
            if url.find(word) != -1:
                return False
            return True

def get_url_from_name(self, name):
    return "https://en.wikipedia.org/wiki/" + name
    
    def get(self, name):
        url = self.get_url_from_name(name)
        page = urllib2.urlopen(url).read()
        soup = bs(page, 'html.parser')
        refs = soup.findAll('a', href=re.compile('/wiki/*'))
        links = map(lambda ref: ref.get('href'), refs)
        links = filter(self.filter, links)
        for link in links:
            print link.split('/')[2]


#parser = Parser()
#parser.get("John_Lennon")
