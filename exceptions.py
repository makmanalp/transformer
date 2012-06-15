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
            index = Schema.resolve_column_ref(self.document, self.column)
            if self.line:
                data = self.line[index]
        return "Parsing Exception:\nLine Number: %s\nCol: %s\nLine: %s\nIdx: %s\nData: %s\nCause: %s\n" %(self.line_number,self.column, self.line, index, data, self.cause)

