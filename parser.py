from bs4 import BeautifulSoup as bs
import requests
import sys
import urllib2
import networkx as nx
from lxml import html
import re


def get_url_from_name(name):
    return "https://en.wikipedia.org/wiki/" + name


def get_links(name):
    url = get_url_from_name(name)
    page = urllib2.urlopen(url).read()
    soup = bs(page, 'html.parser')
    refs = soup.findAll('a', href=re.compile('/wiki/*'))
    for ref in refs:
        print ref

get_links("John_Lennon")
