from transformer import Column, Aggregate, ParsingException

class Schema(object):
    """
    Schemas tell me what input data looks like and how I should process it. For
    example if you have this data:

        age,liabilities,assets,fname   ,lname  ,date
        22 ,0          ,200   ,"George","Lucas",2012-05-02
        55 ,2000       ,40    ,"Oscar" ,"Wilde".2012-02-12

    And you just want everyone and their age, you could use this schema:

        class Person(Schema):
            LastName  = Column("lname")
            Age       = Column("age")
            _ordering = [LastName, Age]

    All schemas contain elements and an ordering list. Each element can be
    [[Column]] like above, or an [[Aggregate]]. Aggregates are combinations of
    Columns, like so:

        FullName = Aggregate(
                    sources=[LastName, Column("fname")]
                    )

    This should return "Lucas George" for the `FullName` column. You can
    specify your own mergers that meld n inputs into one output.  """

    _ordering = []
    """
    The `_ordering` variable tells which fields to include in the output and in
    what order. You don't have to include all the fields you declared.
    """

    @classmethod
    def transform(cls, document, dictionary=False, ignore_empty=True):
        """
        The `transform()` function applies a schema to some data. You can
        specify `dictionary=True` to return each line as a `dict:colname->value`
        rather than a list. You can also specify `ignore_empty` to not process
        empty columns.
        """

        #Headers are not data and are skipped.
        if hasattr(document, "header"):
            document.reader.next()

        """
        If the columns are not given titles, we have to name them
        automatically. To do this, we can traverse upwards from the class MRO,
        looking at each superclass dict for Columns and Aggregates.
        """
        for search_class in reversed(cls.__mro__):
            for k,v in search_class.__dict__.iteritems():
                if isinstance(v, Column) or isinstance(v, Aggregate):
                    if not v.title:
                        v.title = k
        for line_num, line in enumerate(document.reader):
            new_line = []

            """
            Then we process each column and if there is an error, we annotate
            it nicely with line numbers.
            """
            for column in cls._ordering:
                try:
                    if isinstance(column, Column):
                        raw_data = column.fetch_data(document, line)
                        data = column.transform_column(raw_data)
                    elif isinstance(column, Aggregate):
                        raw_datas = column.fetch_data(document, line)
                        data = column.merge_aggregate(raw_datas)
                except ParsingException as pe:
                    pe.document = document
                    pe.line = line
                    pe.line_number = line_num
                    raise pe

                new_data = None
                if data == "":
                    if not ignore_empty:
                        new_data = data
                else:
                    new_data = data

                new_line += [new_data]

            if dictionary:
                yield dict(zip([col.title for col in cls._ordering], new_line))
            else:
                yield new_line

