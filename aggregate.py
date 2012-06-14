from transformer import ParsingException
from transformer import mergers

#TODO: set default merger to concat or someshit
class Aggregate(object):

    def __init__(self, sources=[], merger=mergers.concat(sep="\t"), title=None):
        """Form: Aggregate(sources=[Column(), Column2 ...], merger=None,
        title=None)
        You can specify a previously created column identifier from the schema
        as a source also.
        Merger merges results of each source.
        Title is optional and changes the "header" of the new aggregate.
        """
        self.sources = sources
        self.merger = merger
        self.title = title

    def __repr__(self):
        return "[%s -> %s : %s]" % (self.sources, self.title, self.merger)

    def fetch_data(self, document, line):
        """Given a line and the document it is in, get the data at that line
        that corresponds to this schema column."""
        return [col.fetch_data(document, line) for col in self.sources]

    def merge_aggregate(self, datas):
        try:
            return self.merger.run(datas)
        except Exception as ex:
            raise ParsingException(column=self, cause=ex)
