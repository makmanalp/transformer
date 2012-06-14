
class concat(object):

    def __init__(self, sep=""):
        self.sep = sep

    def run(self, args):
        return self.sep.join([unicode(value) for value in args])
