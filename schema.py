from transformer import Column, ParsingException

class Schema(object):

    _ordering = []

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
                    #TODO:maybe push 2 steps into col class
                    raw_data = column.fetch_data(document, line)
                    data = column.transform_column(raw_data)
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

