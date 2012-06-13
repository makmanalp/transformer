#TODO: set default merger to concat or someshit
class Aggregate(object):

    def __init__(self, *sources, merger=None, title=None):
        self.sources = sources
        self.merger = merger
        self.title = title

    def __repr__(self):
        return "[%s -> %s : %s]" % (self.source, self.title, self.merger)
