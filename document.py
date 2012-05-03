import csv

class Document(object):

    def __init__(self, file):
        self.f = file
        self.get_info()

    def construct_title_xref(self):
        self.title_xref = {}
        for idx, title in enumerate(self.header):
            self.title_xref[title] = idx

    def get_info(self):
        self.sample = self.file.read(2048)
        self.f.seek(0,0) #reset back to beginning for later use
        self.dialect = csv.Sniffer().sniff(self.sample)
        self.reader = csv.reader(self.f, self.dialect)

        if Dialect.has_header(sample):
            self.header = csv.reader(self.f, self.dialect).next()
            self.construct_title_xref()
