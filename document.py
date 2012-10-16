import csv

class Document(object):

    def __init__(self, file, dialect=None, encoding=None):
        self.f = file
        self.dialect = dialect
        self.encoding = encoding
        self.get_info()

    def construct_title_xref(self):
        self.title_xref = {}
        for idx, title in enumerate(self.header):
            self.title_xref[title.lower()] = idx

    def get_info(self):

        self.sample=""
        for x in xrange(0,10):
            self.sample += self.f.readline()

        if not self.dialect:
            self.dialect = csv.Sniffer().sniff(self.sample)
            self.f.seek(0,0) #reset back to beginning for later use

        self.reader = csv.reader(self.f, self.dialect)
        self.f.seek(0,0)

        if csv.Sniffer().has_header(self.sample):
            self.header = csv.reader(self.f, self.dialect).next()
            if self.encoding:
                self.header = [x.decode(self.encoding) for x in self.header]
            self.construct_title_xref()
            self.f.seek(0,0)
