from transformer import Column

class ParsingException(Exception):

    def __init__(self, document, column, line, line_number, cause):
        self.line = line
        self.line_number = line_number
        self.column = column
        self.document = document
        self.cause = cause

    def __str__(self):
        if hasattr(self.document, "header"):
            self.line_number += 1
        index = Schema.resolve_source(self.document, self.column)
        data = self.line[index]
        return "Parsing Exception:\nLine Number: %s\nCol: %s\nLine: %s\nIdx: %s\nData: %s\nCause: %s\n" %(self.line_number,self.column, self.line, index, data, self.cause)

class Schema(object):

    _ordering = []

    @staticmethod
    def resolve_source(document, column):
        if isinstance(column.source, int):
            return column.source
        else:
            return document.title_xref[column.source]

    @classmethod
    def transform(cls, document, dictionary=False, ignore_empty=True):
        if hasattr(document, "header"):
            document.reader.next()

        for k,v in cls.__dict__.iteritems():
            if isinstance(v, Column):
                if not v.title:
                    v.title = k

        for line_num, line in enumerate(document.reader):
            new_line = []
            for column in cls._ordering:
                index = cls.resolve_source(document, column)
                new_data = None
                if line[index] == "":
                    if not ignore_empty:
                        try:
                            new_data = column.transform.run(line[index])
                        except Exception as ex:
                            raise ParsingException(document, column, line, line_num, ex)
                else:
                    try:
                        new_data = column.transform.run(line[index])
                    except Exception as ex:
                        raise ParsingException(document, column, line, line_num, ex)

                new_line += [new_data]
            if dictionary:
                yield dict(zip([col.title for col in cls._ordering], new_line))
            else:
                yield new_line

