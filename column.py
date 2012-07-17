from transformer import transforms
from transformer import ParsingException

class Column(object):

    def __init__(self, source, transform=transforms.identity(), title=None):
        self.source = source
        self.transform = transform
        self.title = title

    def __repr__(self):
        return "[%s -> %s : %s]" % (self.source, self.title, self.transform)

    def resolve_ref(self, document):
        """Columns can be specified as index numbers or as names. If a column
        name is given, this function dereferences it into a numeric column
        index."""
        if isinstance(self.source, int):
            return self.source
        else:
            return document.title_xref[self.source]

    def fetch_data(self, document, line):
        """Given a line and the document it is in, get the data at that line
        that corresponds to this schema column."""
        index = self.resolve_ref(document)
        return line[index]

    def transform_column(self, data):
        try:
            if hasattr(self.transform, "__call__"):
                return self.transform(data)
            else:
                return self.transform.run(data)
        except Exception as ex:
            raise ParsingException(column=self, cause=ex)
