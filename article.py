import parser

class Article(object):
    def __init__(self, name):
        self.name = name

    def links(self):
        return parser.Parser().get(self.name)
