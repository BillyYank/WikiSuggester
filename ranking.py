from article import Article
import collections

class Ranker(object):
    def __init__(self):
        pass

    def getTop(self, name):
        names = collections.defaultdict(int)
        main_article = Article(name)
        for child_name in main_article.links():
            names[child_name] += 1
            child_article = Article(child_name)
            for child2_name in child_article.links():
                names[child2_name] += 1
        print names
        print '---'
        for name in sorted(names, key=names.get, reverse=True):
            print name, names[name]
            
