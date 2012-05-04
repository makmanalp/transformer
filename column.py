from transformer import transforms

class Column(object):

    def __init__(self, source, transform=transforms.identity(), title=None):
        self.source = source
        self.transform = transform
        self.title = title

    def __repr__(self):
        return "[%s -> %s : %s]" % (self.source, self.title, self.transform)
