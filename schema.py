from transformer import Column

class Schema(object):

    _ordering = []

    @classmethod
    def transform(cls, document):
        if hasattr(document, "header"):
            document.reader.next()

        for k,v in cls.__dict__.iteritems():
            if isinstance(v, Column):
                if not v.title:
                    v.title = k

        for line in document.reader:
            new_line = []
            for column in cls._ordering:
                index = -1
                if isinstance(column.source, int):
                    index = column.source
                else:
                    index = document.title_xref[column.source]
                new_data = column.transform.run(line[index])
                new_line += [str(new_data)]
            print new_line

