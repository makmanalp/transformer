from transformer import Column

class ParsingException(Exception):

    def __init__(self, document=None, column=None, line=None, line_number=None, cause=None):
        self.line = line
        self.line_number = line_number
        self.column = column
        self.document = document
        self.cause = cause

    def __str__(self):
        if self.line_number is not None and self.document is not None:
            if hasattr(self.document, "header"):
                self.line_number += 1
        if self.column and self.document:
            index = Schema.resolve_source(self.document, self.column)
            if self.line:
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

    @staticmethod
    def fetch_column(document, column, line):
        index = Schema.resolve_source(document, column)
        return line[index]

    @classmethod
    def transform_column(cls, column, data):
        try:
            return column.transform.run(data)
        except Exception as ex:
            raise ParsingException(column=column, cause=ex)


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

                #For each column, we run the transform for that column (which
                #fetches the data by itself). If there is an error condition, we
                #grab the parsing exception from the transform and annotate it
                #nicely.
                try:
                    raw_data = Schema.fetch_column(document, column, line)
                    data = cls.transform_column(column, raw_data)
                except ParsingException as pe:
                    pe.document = document
                    pe.line = line
                    pe.line_number = line_num

                #If ignore_empty is set, do it
                new_data = None
                if data == "":
                    if not ignore_empty:
                        new_data = data
                else:
                    new_data = data

                #Finally, append to the results for the current line
                new_line += [new_data]

            #If we want the results as a dict, we zip the results with the column names.
            if dictionary:
                yield dict(zip([col.title for col in cls._ordering], new_line))
            else:
                yield new_line

